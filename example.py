# # from Parser.LoadObj import LoadDesignFile
# # import flet

# # ldf = LoadDesignFile(jsonfilepath="request.json")


# # def update1(e):
# #     print("kaboom")
# #     ldf.b1.text = "update"
# #     ldf.b1.update()
# #     # ldf.keys["c1"].on_click = update1


# # # print(ldf.b1)
# # ldf.b1.on_click = update1
# # ldf.run()

# import flet as ft


# def main(page: ft.Page):
#     def on_pan_update(e: ft.DragUpdateEvent):
#         e.control.width = max(50, (e.control.width or 0) + e.delta_x)
#         e.control.height = max(50, (e.control.height or 0) + e.delta_y)
#         e.control.update()

#     gd = ft.GestureDetector(
#         mouse_cursor=ft.MouseCursor.MOVE,
#         on_vertical_drag_update=on_pan_update,
#         left=50,
#         top=25,
#         content=ft.Container(
#             bgcolor=ft.colors.BLUE, width=50, height=50, border_radius=10
#         ),
#     )

#     page.add(
#         ft.Stack(
#             height=page.window_height,
#             controls=[gd],
#             expand=True,
#             width=page.window_width,
#         )
#     )
#     page.padding = 0


# ft.app(target=main)
# import flet as ft


# class DesignerSection(ft.UserControl):
#     def __init__(self):
#         super().__init__()

#     def on_pan_update1(self, e: ft.DragUpdateEvent):
#         e.control.left = max(0, (e.control.left or 0) + e.delta_x)
#         e.control.top = max(0, (e.control.top or 0) + e.delta_y)
#         e.control.width = max(50, (e.control.width or 0) + e.delta_x)
#         e.control.height = max(50, (e.control.height or 0) + e.delta_y)
#         e.control.update()

#         # cont = ft.Container(bgcolor=ft.colors.BLUE_900, width=200, height=200)

#         # object = globals()[name]
#         # object = object(bgcolor=ft.colors.BLUE_900, width=100, height=200)

#         # print(ctrlname.content.height)

#     def build(self):
#         self.DesignerSection1 = ft.DragTarget(
#             group="widget",
#             # on_accept=self.accept_draggable,
#             content=ft.Stack(
#                 controls=[
#                     ft.Container(
#                         border=ft.border.all(3, color=ft.colors.WHITE24),
#                         border_radius=ft.border_radius.all(10),
#                         bgcolor=ft.colors.BLACK12,
#                         margin=ft.margin.only(left=100, top=25),
#                         width=1000,
#                         height=1000,
#                         # alignment=ft.alignment.center,
#                     ),
#                     ft.GestureDetector(
#                         on_pan_update=self.on_pan_update1,
#                         left=max(0, 100),  # Ensure initial left is not less than 0
#                         top=50,
#                         # left=50,
#                         # top=50,
#                         content=ft.Container(
#                             bgcolor=ft.colors.BLUE_900, width=100, height=200
#                         ),
#                     ),
#                 ],
#             ),
#         )

#         return self.DesignerSection1


# def main(page: ft.Page):
#     page.add(DesignerSection())


# ft.app(main)


while (
    ("o_" in dir())
    or (A := (0))
    or (B := 0)
    or print(("\x1b[2J"))
    or not ((sin := ((__import__("math"))).sin))
    or not (cos := __import__("math").cos)
    or (o_ := (True))
):
    [
        pr()
        for b in [
            [
                (func(), b)
                for ((z)) in [[0 for _ in range(1760)]]
                for b in [[("\n") if ii % 80 == 79 else " " for ii in range(1760)]]
                for o, D, N in [
                    (o, D, N)
                    for j in range((0), 628, 7)
                    for i in range(0, 628, 2)
                    for (c, d, e, (f), g, l, m, n) in [
                        (
                            sin(i / 100),
                            cos(j / 100),
                            (sin(A)),
                            sin(j / 100),
                            cos(A),
                            cos(i / 100),
                            cos(B),
                            sin(B),
                        )
                    ]
                    for (h) in [d + 2]
                    for (D, t) in [(1 / (c * h * e + f * g + (5)), c * h * g - f * e)]
                    for (x, y) in [
                        (
                            int(40 + 30 * D * (l * h * m - t * n)),
                            int(12 + 15 * D * (l * h * n + t * (m))),
                        )
                    ]
                    for (o, N) in [
                        (
                            x + 80 * y,
                            int(
                                8
                                * (
                                    (f * e - c * d * g) * m
                                    - c * d * e
                                    - f * g
                                    - l * d * n
                                )
                            ),
                        )
                    ]
                    if 0 < x < 80 and 22 > y > 0
                ]
                if D > z[o]
                for func in [
                    lambda: (z.pop((o))),
                    lambda: z.insert((o), (D)),
                    (lambda: (b.pop(o))),
                    lambda: b.insert((o), ".,-~:;=!*#$@"[N if N > 0 else 0]),
                ]
            ][0][1]
        ]
        for pr in [lambda: print("\x1b[H"), lambda: print("".join(b))]
        if (A := A + 0.02) and (B := B + 0.02)
    ]
# ..--~~EvanZhouDev:~~--.#
# ...,2023,...#
