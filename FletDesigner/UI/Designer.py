import flet as ft
from flet import Container, Row, Column, Text, TextButton, ElevatedButton
from ..Parser.parser import ParserEngine
import json
from ..UI.ToolbarItem import ToolbarItem
from ..widgets.widgets import ALL_WIDGETS
from .Interactive_Manager import IManager
from pynput import keyboard


global current_control_counter_number


# ft.Draggable()
def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


class DesignerSection(ft.UserControl):
    def __init__(
        self, imanager: IManager, project_file_path: str, parser_engine: ParserEngine
    ):
        self.parser_engine = parser_engine
        # self.parser = Parser()
        self.IManager = imanager
        self.name = None
        self.list_file = "widgets/widgets.json"
        self.all_controls = {}
        self.current_control_counter_number = 0
        self.all_regions = {}
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()
        self.selected = None
        self.ctrl_pressed = None
        self.itemName = None
        self.control_to_name = {}
        self.unique_name = None
        self.buttonDown = False
        self.outline_width = 3
        self.outlineContainer = ft.Container(
            border=ft.border.all(color=ft.colors.WHITE, width=self.outline_width),
        )
        self.control_counter = 1
        global current_control_counter_number
        super().__init__()
        self.expand = 3 * 5

    def load_control_list(self):
        self.supported_widgets = []

        self.control_definations = ALL_WIDGETS

    def on_press(self, key):
        if key == keyboard.Key.ctrl:
            self.ctrl_pressed = True

    def on_release(self, key):
        if key == keyboard.Key.ctrl:
            self.ctrl_pressed = False

    # Listen for the ctrl key press and release events

    def buttonDown1(self, e: ft.TapEvent):
        self.buttonDown = True

    def show_outline(self):
        if self.selected is not None:
            self.outlineContainer.left = self.selected.left - self.outline_width
            self.outlineContainer.top = self.selected.top - self.outline_width
            self.outlineContainer.width = self.selected.width + (self.outline_width * 2)
            self.outlineContainer.height = self.selected.height + (
                self.outline_width * 2
            )
            self.outlineContainer.visible = True
            self.outlineContainer.update()
        if self.selected is None:
            self.IManager.select(
                defualt_properties=self.IManager.defualt_properties,
                name="",
                unique_name=self.unique_name,
            )

    def isInRange(self, x, y, region):
        if (
            (x >= region.get("begin_x"))
            and (y >= region.get("begin_y"))
            and (x <= region.get("end_x"))
            and (y <= region.get("end_y"))
        ):
            return True
        return False

    def itemselection(self, e: ft.TapEvent, created_name: str = None):
        self.selected = None  # change and update selected
        # if self.selected is not None:
        self.outlineContainer.visible = False
        self.outlineContainer.update()

        if created_name == None:
            for name, region in self.all_regions.items():
                if self.isInRange(e.local_x, e.local_y, region):
                    item = self.all_controls.get(name)
                    self.selected = item
                    self.itemName = name
                    self.unique_name = name
                    break
        else:
            name = created_name
            item = self.all_controls.get(name)
            self.selected = item
            self.itemName = name

        self.show_outline()
        if self.selected is not None:
            item_properties = {k: v[0] for k, v in item._Control__attrs.items()}
            self.IManager.select(
                defualt_properties=item_properties,
                name=name,
                unique_name=self.unique_name,
            )
        return

    def on_pan_end(self, e: ft.DragEndEvent):
        self.show_outline()

    def on_pan_update(self, e: ft.DragUpdateEvent):
        if self.selected == None:
            return
        full_width = self.page.window_width * (3 / 5)
        full_height = 1290  # self.page.window_height #1290 # issue is here
        self.outlineContainer.visible = False
        self.outlineContainer.update()
        self.new_left = clamp(
            (self.selected.left if self.selected else 0) + e.delta_x,
            0 + 5,
            full_width - (self.selected.width * 0.92) - 5,
        )
        self.new_top = clamp(
            (self.selected.top or 0) + e.delta_y,
            0 + 5,
            full_height - (self.selected.height * 1.75) - 35,
        )
        # print(self.itemName)
        self.all_regions.update(  # key us tommorow
            {
                self.itemName: {
                    "begin_x": self.new_left,
                    "begin_y": self.new_top,
                    "end_x": self.new_left + self.selected.width,
                    "end_y": self.new_top + self.selected.height,
                }
            }
        )
        self.selected.left = self.new_left
        self.selected.top = self.new_top
        self.selected.update()
        # print(self.ctrl_pressed)

        # Edit & Update the Control Positioning Property via the Parser
        self.parser_engine.edit_control_property(
            control_uniqe_name=str(self.itemName),
            property_name="top",
            new_property_value=int(self.new_top),
        )

        self.parser_engine.edit_control_property(
            control_uniqe_name=str(self.itemName),
            property_name="left",
            new_property_value=int(self.new_left),
        )

    def accept_draggable(self, e: ft.DragTargetAcceptEvent):
        global current_control_counter_number
        ctrlname = e.page.get_control(e.src_id)
        self.name = ctrlname.content.content.value
        control_data = next(
            (item for item in self.control_definations if item.get(self.name)), None
        )

        self.IManager.nmn = self.name

        if control_data is None:
            print("Control will be added later")
            return
        self.load_control_list()
        default_properties = control_data[self.name]["default"]
        object = globals()[self.name]
        object = object(**default_properties)
        current_control_counter_number = (
            self.parser_engine.get_new_control_counter_number()
        )
        self.unique_name = f"{self.name}{current_control_counter_number}"
        # print(self.unique_name)
        self.all_controls.update({self.unique_name: object})

        self.all_regions.update(
            {
                self.unique_name: {
                    "begin_x": object.left,
                    "begin_y": object.top,
                    "end_x": object.left + object.width,
                    "end_y": object.top + object.height,
                }
            }
        )
        self.main_stack.controls.append(
            list(self.all_controls.values())[current_control_counter_number - 1]
        )
        e.control.update()
        self.main_stack.update()
        self.itemselection("", self.unique_name)

        # Make The Parser Save This New Control.
        self.parser_engine.add_new_control_to_content(
            control_uniqe_name=str(self.unique_name),
            control_dict=dict(control_data[self.name]["default"]),
            control_class_name=str(self.name),
        )

    def build(self):
        self.load_control_list()
        self.main_stack = ft.Stack(
            controls=[
                ft.Container(
                    expand=True,
                    border=ft.border.all(1.9, color="#383838"),
                    border_radius=ft.border_radius.all(8),
                    bgcolor=ft.colors.BLACK,
                ),
                self.outlineContainer,
            ],
            expand=True,
        )
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.GestureDetector(
                expand=True,
                content=self.main_stack,
                on_tap_down=self.buttonDown1,
                on_pan_update=self.on_pan_update,
                on_pan_end=self.on_pan_end,
                on_tap_up=self.itemselection,
            ),
        )

        # Load the saved control to the deigner
        self.parser_engine.load_content(designer_section_class=self)

        return self.DesignerSection1

    def add_control_to_designer(self, control):
        pass
