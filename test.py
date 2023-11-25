# import flet as ft
# import json

# all_controls = {}
# all_regions = {}
# selected = None
# itemName = None
# buttonDown = False
# # list_file = "widgets/widgets_list.json"
# # with open(list_file, "rb") as f:
# #     supportedControls = list(map(lambda x: list(x.keys())[0], json.loads(f.read())))
# outlineContainer = ft.Container(
#     border=ft.border.all(color=ft.colors.DEEP_ORANGE_900, width=3),
# )


# def isInRange(x, y, region):
#     if (
#         (x >= region.get("begin_x"))
#         and (y >= region.get("begin_y"))
#         and (x <= region.get("end_x"))
#         and (y <= region.get("end_y"))
#     ):
#         return True
#     return False


# def main(page: ft.Page):
#     global outlineContainer

#     page.window_height = 1000
#     page.window_width = 1000

#     def show_outline(selected):
#         global outlineContainer
#         outlineContainer.left = selected.left
#         outlineContainer.top = selected.top
#         outlineContainer.width = selected.width
#         outlineContainer.height = selected.height
#         outlineContainer.visible = True
#         outlineContainer.update()

#     def buttonDown(e: ft.TapEvent):
#         global buttonDown
#         buttonDown = True

#     def itemselection(e: ft.TapEvent):
#         global buttonDown
#         if not buttonDown:
#             return
#         global all_controls
#         global all_regions
#         global selected
#         global itemName
#         global outlineContainer

#         selected = None
#         outlineContainer.visible = False
#         outlineContainer.update()
#         for name, region in all_regions.items():
#             if isInRange(e.local_x, e.local_y, region):
#                 item = all_controls.get(name)
#                 selected = item
#                 itemName = name
#                 break
#         if selected == None:
#             return
#         show_outline(selected=selected)
#         return

#     def on_pan_update2(e: ft.DragUpdateEvent):
#         global left_pressed
#         global selected
#         global itemName
#         global outlineContainer

#         if selected == None:
#             print("kslalsd")
#             return
#         outlineContainer.visible = False
#         outlineContainer.update()
#         new_left = max(0, (selected.left or 0) + e.delta_x)
#         new_top = max(0, (selected.top or 0) + e.delta_y)
#         all_regions.update(
#             {
#                 itemName: {
#                     "begin_x": new_left,
#                     "begin_y": new_top,
#                     "end_x": new_left + selected.width,
#                     "end_y": new_top + selected.height,
#                 }
#             }
#         )
#         selected.left = new_left
#         selected.top = new_top
#         selected.update()
#         show_outline(selected=selected)


#     main_stack = ft.Stack(
#         controls=[
#             ft.Container(
#                 border=ft.border.all(1.9, color="#383838"),
#                 border_radius=ft.border_radius.all(8),
#                 bgcolor=ft.colors.BLACK,
#                 margin=ft.margin.only(left=0, top=0),
#             )
#         ],
#         height=1000,
#         width=1000,
#     )
#     for item in all_controls.values():
#         main_stack.controls.append(item)
#     main_stack.controls.append(outlineContainer)
#     gd1 = ft.GestureDetector(
#         mouse_cursor=ft.MouseCursor.MOVE,
#         drag_interval=5,
#         on_pan_update=on_pan_update2,
#         on_tap_down=buttonDown,
#         on_tap_up=itemselection,
#         width=1000,
#         height=1000,
#         # left=4000,
#         # top=1500,
#         content=main_stack,
#     )

#     # gd2 = ft.GestureDetector(
#     #     mouse_cursor=ft.MouseCursor.MOVE,
#     #     on_long_press_start=on_long_press,
#     #     on_pan_update=on_pan_update2,
#     #     drag_interval=10,
#     #     on_tap=on_tap1,
#     #     on_long_press_end=on_long_press,
#     #     left=700,
#     #     top=300,
#     #     content=ft.Container(
#     #         # bgcolor=ft.colors.BLUE,
#     #         width=row2.height,
#     #         height=row2.height,
#     #         content=row2,
#     #     ),
#     # )
#     # stack = ft.Stack([gd1], width=4000, height=1500)

#     page.add(gd1)
#     main_stack.update()


# ft.app(target=main)


# #  # def __init__(self, conn: Connection, session_id):
# #     #     super(ft.Page).__init__(conn, session_id)
# #     container = None


import flet as ft

from ColorPicker.color_picker import ColorPicker


class test(ft.UserControl):
    def __init__(self):
        super().__init__()

    def change_color(self, e):
        self.check.bgcolor = self.color_picker.color

    def build(self):
        self.check = ft.Container(width=50, height=50)
        self.color_picker = ColorPicker(color="#c8df6f", on_change=self.change_color)

        test = ft.Column(controls=[self.color_picker, self.check])

        return test


def main(page: ft.Page):
    check = ft.Container(width=50, height=50)

    def change_color(e):
        check.bgcolor = color_picker.color
        check.update()

    color_picker = ColorPicker(color="#c8df6f", on_change=change_color)
    page.add(color_picker, check)

    page.update()


ft.app(target=main)
