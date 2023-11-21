import flet as ft
from flet import Container, Row, Column, Text, TextButton
from Parser.Parserengine import Parser
import json
from UI.ToolbarItem import ToolbarItem

ft.TextButton


# ft.Draggable()
def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


class DesignerSection(ft.UserControl):
    def __init__(self, window_width):
        self.parser = Parser()
        self.window_width = window_width
        self.list_file = "widgets/widgets.json"
        self.all_controls = {}
        self.all_regions = {}
        self.selected = None
        self.itemName = None
        self.buttonDown = False
        self.outline_width = 3
        self.outlineContainer = ft.Container(
            border=ft.border.all(color=ft.colors.WHITE, width=self.outline_width),
        )
        self.control_counter = 1
        super().__init__()

    def load_control_list(self):
        self.supported_widgets = []
        with open(self.list_file, "rb") as f:
            self.control_definations = json.load(fp=f)

            # print(self.supportedControls[0])

    def buttonDown1(self, e: ft.TapEvent):
        self.buttonDown = True

    def show_outline(self):
        self.outlineContainer.left = self.selected.left - self.outline_width
        self.outlineContainer.top = self.selected.top - self.outline_width
        self.outlineContainer.width = self.selected.width + (self.outline_width * 2)
        self.outlineContainer.height = self.selected.height + (self.outline_width * 2)
        self.outlineContainer.visible = True
        self.outlineContainer.update()

    def isInRange(self, x, y, region):
        if (
            (x >= region.get("begin_x"))
            and (y >= region.get("begin_y"))
            and (x <= region.get("end_x"))
            and (y <= region.get("end_y"))
        ):
            return True
        return False

    def itemselection(self, e: ft.TapEvent):
        self.selected = None
        self.outlineContainer.visible = False
        self.outlineContainer.update()
        for name, region in self.all_regions.items():
            if self.isInRange(e.local_x, e.local_y, region):
                item = self.all_controls.get(name)
                self.selected = item
                self.itemName = name
                break
        if self.selected == None:
            return
        self.show_outline()
        return

    def on_pan_end(self, e: ft.DragEndEvent):
        if self.selected == None:
            return
        self.show_outline()

    def on_pan_update(self, e: ft.DragUpdateEvent):
        if self.selected == None:
            return
        self.outlineContainer.visible = False
        self.outlineContainer.update()
        self.new_left = clamp(
            (self.selected.left or 0) + e.delta_x,
            0 + 5,
            e.control.content.width - self.selected.width - 5,
        )
        self.new_top = clamp(
            (self.selected.top or 0) + e.delta_y,
            0 + 5,
            e.control.content.height - (self.selected.height * 2) - 35,
        )
        self.all_regions.update(
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

    def accept_draggable(self, e: ft.DragTargetAcceptEvent):
        ctrlname = e.page.get_control(e.src_id)
        name = ctrlname.content.content.value
        control_data = next(
            (item for item in self.control_definations if item.get(name)), None
        )
        if control_data is None:
            print("Control will be added later")
            return
        self.load_control_list()
        print(name)
        default_properties = control_data[name]["default"]
        object = globals()[name]
        object = object(**default_properties)
        unique_name = f"container{self.control_counter}"
        self.all_controls.update({unique_name: object})
        self.all_regions.update(
            {
                unique_name: {
                    "begin_x": object.left,
                    "begin_y": object.top,
                    "end_x": object.left + object.width,
                    "end_y": object.top + object.height,
                }
            }
        )
        (
            self.main_stack.controls.append(
                list(self.all_controls.values())[self.control_counter - 1]
            )
        )
        self.control_counter += 1
        e.control.update()
        self.main_stack.update()

    def build(self):
        width = ((6 / 10) * self.window_width)
        self.load_control_list()
        self.main_stack = ft.Stack(
            controls=[
                ft.Container(
                    width=width,
                    height=1290,
                    border=ft.border.all(1.9, color="#383838"),
                    border_radius=ft.border_radius.all(8),
                    bgcolor=ft.colors.BLACK,
                    # alignment=ft.alignment.center,
                ),
                self.outlineContainer,
            ],
            width=width,
            height=1290,
        )
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.GestureDetector(
                width=width,
                height=1290,
                content=self.main_stack,
                on_tap_down=self.buttonDown1,
                on_pan_update=self.on_pan_update,
                on_pan_end=self.on_pan_end,
                on_tap_up=self.itemselection,
            ),
        )
        return self.DesignerSection1
