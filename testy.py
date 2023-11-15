import flet as ft


async def main(page: ft.Page):
    async def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        if page.route == "/":
            test = ft.Text("hi")

            # Define your controls here

            nav_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.EXPLORE, label="nav 0"),
                    ft.NavigationDestination(icon=ft.icons.EXPLORE, label="nav 1"),
                ],
                selected_index=1,
            )

            async def update_onchange(e, nav_bar=nav_bar):
                test.value = nav_bar.selected_index
                # Now you can access the controls inside this function
                await test.update_async()

            view = ft.View(
                route="/",
                navigation_bar=nav_bar,
                horizontal_alignment="center",
                padding=ft.padding.all(0),
            )
            view.controls.append(test)  # Add the test control to the view
            page.views.append(view)
            nav_bar.on_change = update_onchange

        await page.update_async()
        print(page.views)

    async def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        await page.go_async(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    await page.go_async("/")
    await page.update_async()


ft.app(target=main)
