import flet as ft

from Parser1.Parserengine import *

import sys


# Parser()


# ft.Draggable()


class DesignerSection(ft.UserControl):
    def __init__(self):
        super().__init__()

    def accept_draggable(self, e: ft.DragTargetAcceptEvent):
        src = e.data

        id = src[1:14][10:]

        if id == "_33":
            print("verified")

    def build(self):
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.Stack(
                width=1200,
                height=1000,
                controls=[
                    ft.Container(
                        border=ft.border.all(width=3, color=ft.colors.WHITE12),
                        border_radius=ft.border_radius.all(10),
                        bgcolor=ft.colors.BLACK12,
                        margin=ft.margin.only(left=100, top=25),
                    ),
                ],
            ),
        )

        return self.DesignerSection1
