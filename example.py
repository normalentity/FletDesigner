# from Parser.LoadObj import LoadDesignFile
# import flet

# ldf = LoadDesignFile(jsonfilepath="request.json")


# def update1(e):
#     print("kaboom")
#     ldf.b1.text = "update"
#     ldf.b1.update()
#     # ldf.keys["c1"].on_click = update1


# # print(ldf.b1)
# ldf.b1.on_click = update1
# ldf.run()

import flet as ft


def main(page: ft.Page):
    def on_pan_update(e: ft.DragUpdateEvent):
        e.control.width = max(50, (e.control.width or 0) + e.delta_x)
        e.control.height = max(50, (e.control.height or 0) + e.delta_y)
        e.control.update()

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        on_vertical_drag_update=on_pan_update,
        left=50,
        top=25,
        content=ft.Container(
            bgcolor=ft.colors.BLUE, width=50, height=50, border_radius=10
        ),
    )

    page.add(
        ft.Stack(
            height=page.window_height,
            controls=[gd],
            expand=True,
            width=page.window_width,
        )
    )
    page.padding = 0


ft.app(target=main)
