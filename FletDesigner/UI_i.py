import flet as ft
import time

# from ..FletDesigner.
from .UI.DesignPage import DesignPage


class MainDesigner:
    def __init__(self, file_path:str) -> None:
        self.file_path = file_path
        ft.app(target=self.app)
    
    def app (self, page:ft.Page):
        # Store the page as a class property
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
            design_page = DesignPage(
                project_file_path=self.file_path
            )
            page.views.append(design_page.build())
            page.update()