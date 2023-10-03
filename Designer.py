import flet as ft
from flet import Container
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
        name = ctrlname.content.content.value

        # cont = ft.Container(bgcolor=ft.colors.BLUE_900, width=200, height=200)

        object = globals()[name]
        object = object(bgcolor=ft.colors.BLUE_900, width=100, height=200)
        e.control.content.controls[0].content = ft.Container(content=[object])

        e.control.update()
        # print(ctrlname.content.height)

    def build(self):
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        border=ft.border.all(3, color=ft.colors.WHITE24),
                        border_radius=ft.border_radius.all(10),
                        bgcolor=ft.colors.BLACK12,
                        margin=ft.margin.only(left=100, top=25),
                        width=1200,
                        height=1000,
                        # alignment=ft.alignment.center,
                    ),
                ],
            ),
        )

        return self.DesignerSection1
