import flet as ft
from UI.ToolbarItems import ToolbarItems

class Toolbar(ft.UserControl):
    def __init__(self, ToolbarItems: ToolbarItems):
        self.toolbaritems = ToolbarItems
        super().__init__()

    def build(self):
        self.toolbar = ft.Container(
            animate_scale=ft.animation.Animation(5000, ft.AnimationCurve.BOUNCE_OUT),
            width=225,
            border_radius=ft.border_radius.all(5),
            height=1700,
            bgcolor=ft.colors.with_opacity(opacity=1, color="#1e2124"),
            blur=ft.Blur(200, 200, ft.BlurTileMode.MIRROR),
            shadow=ft.BoxShadow(
                200,
                200,
                ft.colors.with_opacity(opacity=1, color="#1e2124"),
                ft.Offset(55, 200),
                ft.ShadowBlurStyle.INNER,
            ),
            padding=ft.padding.all(5),
            content=self.toolbaritems,
        )

        return self.toolbar
