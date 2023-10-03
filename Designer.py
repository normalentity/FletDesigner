import flet as ft
from Parser.Parserengine import Parser

from UI.ToolbarItem import ToolbarItem

# ft.Draggable()


class DesignerSection(ft.UserControl):
    def __init__(self):
        self.parser = Parser()
        super().__init__()

    def accept_draggable(self, e: ft.DragTargetAcceptEvent):
        # self.parser.AddWidget()
        getcrlname = e.control
        ctrlname = e.page.get_control(e.src_id)
        print(ctrlname.content.content.value)
        print(ctrlname.content.height)

    def build(self):
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.Stack(
                width=1200,
                height=1000,
                controls=[
                    ft.Container(
                        border=ft.border.all(3, color=ft.colors.WHITE24),
                        border_radius=ft.border_radius.all(10),
                        bgcolor=ft.colors.BLACK12,
                        margin=ft.margin.only(left=100, top=25),
                    ),
                ],
            ),
        )

        return self.DesignerSection1
