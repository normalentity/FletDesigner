import flet as ft
from time import sleep


from UI.animationpage import __view__
from UI.DesignPage import DesignPage


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window_maximized = True
    # page.window_full_screen = False

    # page.go("/welcome")
    page.go(route="/design")

    def routechange(e: ft.RouteChangeEvent):
        # if page.route == "/welcome":
        #     page.views.clear()
        #     index = __view__()
        #     page.views.append(index.build())
        #     page.update()
        #     sleep(1)
        #     index.randomize("None")
        #     sleep(1)
        #     index.assemble("None")
        #     sleep(2.5)

        
        if page.route == "/design":
            
            design_page = DesignPage()
            page.views.append(design_page.build())
            page.update()
            # page.on_resize

    page.bgcolor = ft.colors.BLACK
    page.on_route_change = routechange

    page.update()


if __name__ == "__main__":
    ft.app(main)
