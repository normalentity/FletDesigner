import flet as ft

# ft.Draggable()


class DesignerSection(ft.UserControl):
    def __init__(self):
        super().__init__()

    def accept_draggable(self, e: ft.DragTargetAcceptEvent):
        src = self._get_control_name()
        e.control.content.content = ft.Container(
            bgcolor=ft.colors.BLUE_700,
            width=50,
            height=50,
            # border=ft.border.all(3, color=ft.colors.CYAN_300),
            # border_radius=ft.border_radius.all(10),
            # margin=ft.margin.only(left=100, top=25),
        )
        e.control.update()

    def build(self):
        self.DesignerSection1 = ft.DragTarget(
            group="widget",
            on_accept=self.accept_draggable,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        width=1200,
                        height=1000,
                        border=ft.border.all(3, color=ft.colors.CYAN_300),
                        border_radius=ft.border_radius.all(10),
                        bgcolor=ft.colors.BLACK12,
                        margin=ft.margin.only(left=100, top=25),
                    ),
                ]
            ),
        )

        return self.DesignerSection1
