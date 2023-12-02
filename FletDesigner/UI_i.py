import flet as ft
import time

# from ..FletDesigner.
from .UI.DesignPage import DesignPage


class Main:
    def __init__(self, page: ft.Page) -> None:
        self.page: ft.Page = page

        # Set Page Props
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = ft.colors.BLACK
        page.window_maximized = True

        # Set Page Events
        page.on_route_change = self.routechange

        # Update page
        page.go(route="/design")
        page.update()

    def routechange(self, e):
        page = self.page
        if page.route == "/design":
            design_page = DesignPage()
            page.views.append(design_page.build())
            page.update()


if __name__ == "__main__":
    ft.app(Main)
