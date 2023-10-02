import flet as ft


class ToolbarItem(ft.UserControl):
    def __init__(self, text):
        self.text = text
        self.selected = False
        self.container = ft.Container(
            bgcolor=ft.colors.GREY_700,
            height=40,
            border_radius=8,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            padding=ft.padding.all(10),
            animate=200,
            alignment=ft.alignment.center,
            content=ft.Text(
                self.text,
                size=16,
                style=ft.TextStyle(weight=ft.FontWeight.W_900, font_family="Helvetica"),
                text_align=ft.TextAlign.JUSTIFY,
            ),
        )
        super().__init__()

    def build(self):
        self.toolbaritem = ft.Draggable(
            group="widget",
            content_feedback=ft.Container(
                width=20,
                height=20,
                content=ft.Icon(name=ft.icons.ADD, color=ft.colors.BLUE_300),
            ),
            content=self.container,
        )
        return self.toolbaritem

    def add_selectionchanged_callback(self, callback):
        self.container.on_click = callback
