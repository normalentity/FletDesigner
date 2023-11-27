import flet as ft
import time

from .UI.animationpage import __view__
from .UI.DesignPage import DesignPage



class Main:
    def __init__(self, page:ft.Page) -> None:
        self.page : ft.Page = page

        # Set Page Props
        page.window_width = 800
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = ft.colors.BLACK

        # Set Page Events
        page.on_route_change = self.routechange

        # Update page
        page.go("/welcome")
        page.update()

    def routechange (self, e):
        page = self.page
        page.go(route="/design")
        if page.route == "/design":
            # page.window_maximized = True
            page.window_full_screen = True
            page.update()
            time.sleep(1)
            window_width1 = page.window_width
            page.update()
            design_page = DesignPage(window_width1=window_width1)
            page.views.clear()
            page.update()
            # page.window_full_screen = True
            time.sleep(0.3)
            page.views.append(design_page.build())
            page.update()
            page.on_resize



if __name__ == "__main__":
    ft.app(Main)
