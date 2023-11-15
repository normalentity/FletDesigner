import flet as ft
from flet import Container
from Parser.Parserengine import Parser
import json
from UI.ToolbarItem import ToolbarItem

# ft.Draggable()


class DesignerSection(ft.UserControl):
    def __init__(self):
        self.parser = Parser()
        self.list_file = "widgets/widgets_list.json"
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
        with open(self.list_file, "rb") as f:
            self.supportedControls = list(
                map(lambda x: list(x.keys())[0], json.loads(f.read()))
            )

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
        self.show_outline()

    def on_pan_update(self, e: ft.DragUpdateEvent):
        if self.selected == None:
            return
        self.outlineContainer.visible = False
        self.outlineContainer.update()
        self.new_left = max(80, (self.selected.left or 0) + e.delta_x)
        self.new_top = max(30, (self.selected.top or 0) + e.delta_y)
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
        object = globals()[name]
        object = object(
            bgcolor=ft.colors.RED,
            width=100,
            height=200,
            left=200 + (self.control_counter+5),
            top=200,
        )
        unique_name = f"container{self.control_counter}"
        print(unique_name)
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
        self.main_stack = ft.Stack(
            controls=[
                ft.Container(
                    border=ft.border.all(1.9, color="#383838"),
                    border_radius=ft.border_radius.all(8),
                    bgcolor=ft.colors.BLACK,
                    # alignment=ft.alignment.center,
                ),
                self.outlineContainer,
            ],
        )
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.GestureDetector(
                width=1200,
                height=1290,
                content=self.main_stack,
                on_tap_down=self.buttonDown1,
                on_pan_update=self.on_pan_update,
                on_pan_end=self.on_pan_end,
                on_tap_up=self.itemselection,
            ),
        )
        return self.DesignerSection1
