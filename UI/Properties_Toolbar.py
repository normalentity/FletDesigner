import flet as ft
from time import sleep
from ColorPicker.color_picker import ColorPicker

# from flet_contrib.color_picker import


class PropertiesToolbar(ft.UserControl):
    pass

    def __init__(self, page):
        self.page = page
        super().__init__()

    def open_alert_dlg(self, e):
        self.page.dialog = self.color_picker_modal
        self.color_picker_modal.open = True
        self.page.update()

    def use_color(self, e):
        self.color_holder.bgcolor = self.color_picker.color
        self.hex_holder.content.value = self.color_picker.color
        self.color_holder.update()
        self.hex_holder.content.update()
        self.color_picker_modal.open = False
        self.color_holder.update()
        self.page.update()

    def close_dlg(self, e):
        # self.page.dialog = self.color_picker_modal
        self.color_picker_modal.open = False
        self.page.update()

    def build(self):
        self.propertiesContainer = ft.Container(
            width=460,
            height=1200,
            bgcolor=ft.colors.with_opacity(opacity=0.6, color=ft.colors.BLACK45),
            border_radius=ft.border_radius.all(15),
            # padding=ft.padding.only(left=15, right=15, top=30),
        )

        self.propertiesColumn = ft.Column(controls=[ft.Stack()], scroll="always")

        heading = ft.Container(
            margin=ft.margin.only(top=5, left=10),
            content=ft.Text(value="Properties:", size=25),
        )
        heading_Control_name = ft.Container(
            margin=ft.margin.only(top=60, left=10),
            content=ft.Row(
                controls=[
                    ft.Text(value="Control Name", size=15, height=20),
                ]
            ),
        )
        # tight=True,

        heading_width = ft.Row(
            controls=[
                ft.Container(
                    margin=ft.margin.only(left=270, top=155),
                    content=ft.Row(
                        controls=[
                            ft.Text(value="Width", size=15, height=20),
                        ]
                    ),
                )
            ],
        )

        heading_height = ft.Container(
            margin=ft.margin.only(top=155, left=10),
            content=ft.Row(
                controls=[
                    ft.Text(value="Height", size=15, height=20),
                ]
            ),
        )
        # spacing=1,

        heading_color = ft.Row(
            # spacing=1,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=260, left=10),
                    content=ft.Text(value="Color", size=15, height=20),
                )
            ],
        )
        self.color_holder = ft.Container(
            width=20,
            height=20,
            bgcolor=ft.colors.RED,
            border_radius=5,
            margin=ft.margin.only(left=10),
            on_click=self.open_alert_dlg,
            # ink=True,
        )

        output_color = ft.Container(width=60, height=60, border_radius=5)

        self.color_picker = ColorPicker(color="#c8df6f", width=300)
        self.color_picker_modal = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=6),
            content=self.color_picker,
            actions=[
                ft.Container(
                    width=90,
                    height=36,
                    # margin=ft.margin.only(top=130),
                    bgcolor=ft.colors.WHITE30,
                    alignment=ft.alignment.center,
                    border_radius=8,
                    ink=True,
                    on_click=self.close_dlg,
                    content=ft.Text("Cancel", size=16),
                ),
                ft.Container(
                    width=90,
                    height=38,
                    # margin=ft.margin.only(top=130),
                    bgcolor=ft.colors.BLACK,
                    alignment=ft.alignment.center,
                    border_radius=8,
                    ink=True,
                    on_click=self.use_color,
                    content=ft.Text("Use Color", size=16),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.hex_holder = ft.Container(content=ft.Text(value="#ff0000", size=16))
        self.color_box = ft.Container(
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                # margin=ft.margin.only(left=10, top=290),
                border_radius=7,
                content=ft.Row(controls=[self.color_holder, self.hex_holder]),
                margin=ft.margin.only(left=10, top=290),
            )
        )

        self.control_name_space = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                # content_padding=ft.padding.only(left=5, right=80),
                label="Control Name",
                width=380,
            ),
            margin=ft.margin.only(left=10, top=90),
        )

        self.control_width = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=190,
                # content_padding=ft.padding.only(left=5, right=5),
                label="Width",
            ),
            margin=ft.margin.only(left=270, top=190),
        )

        self.control_height = ft.Container(
            content=ft.Container(
                width=190,
                content=ft.TextField(
                    # text_align=ft.alignment.center,
                    width=190,
                    # content_padding=ft.padding.only(left=5, right=15, top=30),
                    label="Height",
                ),
            ),
            margin=ft.margin.only(left=15, top=185),
        )
        self.propertiesColumn.controls[0].controls = [
            heading,
            heading_width,
            self.control_width,
            heading_Control_name,
            heading_height,
            self.control_name_space,
            self.color_box,
            self.control_height,
            heading_color,
        ]

        self.propertiesContainer.content = self.propertiesColumn

        return self.propertiesContainer
