import flet as ft
from flet import Container
from Parser.Parserengine import Parser

from UI.ToolbarItem import ToolbarItem

# ft.Draggable()


class DesignerSection(ft.UserControl):
    def __init__(self):
        self.parser = Parser()
        super().__init__()

    def on_pan_update1(self, e: ft.DragUpdateEvent):
        # e.control.left = max(0, (e.control.left or 0) + e.delta_x)
        # e.control.top = max(0, (e.control.top or 0) + e.delta_y)
        e.control.width = max(50, (e.control.width or 0) + e.delta_x)
        e.control.height = max(50, (e.control.height or 0) + e.delta_y)
        e.control.update()

    def accept_draggable(self, e: ft.DragTargetAcceptEvent):
        ctrlname = e.page.get_control(e.src_id)
        name = ctrlname.content.content.value
        self.container = e.control.content.controls
        object = globals()[name]
        object = object(bgcolor=ft.colors.RED, width=100, height=200)
        self.container.append(
            ft.GestureDetector(
                on_pan_update=self.on_pan_update1,
                left=max(0, 100),  # Ensure initial left is not less than 0
                top=50,
                content=object,
            )
        )

        e.control.update()

    def build(self):
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        border=ft.border.all(3, color="#383838"),
                        border_radius=ft.border_radius.all(8),
                        bgcolor=ft.colors.BLACK12,
                        margin=ft.margin.only(left=75, top=25),
                        width=1000,
                        height=1000,
                        # alignment=ft.alignment.center,
                    ),
                ],
            ),
        )

        return self.DesignerSection1
