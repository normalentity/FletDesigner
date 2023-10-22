import flet as ft
from UI.ToolbarItems import ToolbarItems


class Toolbar(ft.UserControl):
    def __init__(self, ToolbarItems: ToolbarItems):
        self.toolbaritems = ToolbarItems
        super().__init__()

    def build(self):
        # The Tool bar for dragging the Controls to the Designer Section
        self.toolbar = ft.Container(
            animate_scale=ft.animation.Animation(5000, ft.AnimationCurve.BOUNCE_IN),
            width=220,
            border_radius=ft.border_radius.all(3),
            height=1700,
            bgcolor=ft.colors.with_opacity(opacity=1, color="#1e1e1e"),
            blur=ft.Blur(200, 200, ft.BlurTileMode.MIRROR),
            shadow=ft.BoxShadow(
                200,
                200,
                ft.colors.with_opacity(opacity=1, color= "#1e1e1e"),
                ft.Offset(55, 200),
                ft.ShadowBlurStyle.INNER,
            ),
            padding=ft.padding.all(5),
            content=self.toolbaritems,
        )

        return self.toolbar
