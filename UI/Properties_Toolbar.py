import multiprocessing
import flet as ft
from ColorPicker.color_picker import ColorPicker

# ft.Dis


# ft.SweepGradient()
ft.Container()


class PropertiesToolbar(ft.UserControl):
    def __init__(self, page,):# window_width):
        self.page = page
        # self.window_width = window_width
        super().__init__()
        self.expand = int((1 + 0.2) * 5)

    def on_change(self, e):
        self.selection_value = e.control.value
        if self.selection_value == "LinearGradient":
            pass

    def open_alert_dlg(self, e):
        self.page.dialog = self.color_picker_modal
        self.color_picker_modal.open = True
        self.page.update()

    def open_alert_dlg1(self, e):
        self.page.dialog = self.color_picker_modal1
        self.color_picker_modal1.open = True
        self.page.update()

    def open_alert_dlg2(self, e):
        self.page.dialog = self.color_picker_modal2
        self.color_picker_modal2.open = True
        self.page.update()

    def use_color(self, e):
        self.color_holder.bgcolor = self.color_picker.color
        self.hex_holder.content.value = self.color_picker.color
        self.color_holder.update()
        self.hex_holder.content.update()
        self.color_picker_modal.open = False
        self.color_holder.update()
        self.page.update()

    def use_color_gradient(self, e):
        self.gradient_color_holder.bgcolor = self.color_picker1.color
        self.gradient_hex_holder.content.value = self.color_picker1.color
        self.gradient_color_holder.update()
        self.gradient_hex_holder.content.update()
        self.color_picker_modal1.open = False
        self.gradient_color_holder.update()
        self.page.update()

    def use_color_gradient1(self, e):
        self.gradient_color_holder1.bgcolor = self.color_picker2.color
        self.gradient_hex_holder1.content.value = self.color_picker2.color
        self.gradient_color_holder1.update()
        self.gradient_hex_holder1.content.update()
        self.color_picker_modal2.open = False
        self.gradient_color_holder1.update()
        self.page.update()

    def close_dlg(self, e):
        self.color_picker_modal.open = False
        self.page.update()

    def close_dlg1(self, e):
        self.color_picker_modal1.open = False
        self.page.update()

    def close_dlg2(self, e):
        self.color_picker_modal2.open = False
        self.page.update()

    def build(self):
        # (existing build code)

        self.propertiesContainer = ft.Container(
            # width=((2.5 / 10) * self.window_width),
            height=1200,
            bgcolor=ft.colors.with_opacity(opacity=0.6, color=ft.colors.BLACK45),
            border_radius=ft.border_radius.all(15),
            # padding=ft.padding.only(left=15, right=15, top=30),
        )

        self.propertiesColumn = ft.Column(controls=[ft.Stack()], scroll="always")

        heading = ft.Container(
            margin=ft.margin.only(top=10),
            alignment=ft.alignment.center,
            content=ft.Text(value="Properties", size=20),
        )
        heading_Control_name = ft.Container(
            margin=ft.margin.only(top=60, left=10),
            content=ft.Row(
                controls=[
                    ft.Text(value="Control Name", size=15),
                ]
            ),
        )
        # tight=True,

        heading_width = ft.Row(
            controls=[
                ft.Container(
                    margin=ft.margin.only(left=160, top=155),
                    content=ft.Row(
                        controls=[
                            ft.Text(value="Width", size=15),
                        ]
                    ),
                )
            ],
        )

        heading_height = ft.Container(
            margin=ft.margin.only(top=155, left=10),
            content=ft.Row(
                controls=[
                    ft.Text(value="Height", size=15),
                ]
            ),
        )

        # spacing=1,

        heading_color = ft.Row(
            # spacing=1,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=260, left=10),
                    content=ft.Text(value="Color", size=15),
                )
            ],
        )
        heading_gradient = ft.Row(
            # spacing=1,
            alignment=ft.alignment.center,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=330, left=10),
                    content=ft.Text(value="Gradient", size=15),
                    alignment=ft.alignment.center,
                )
            ],
        )
        heading_beign = ft.Row(
            # spacing=1,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=75, left=200),
                    content=ft.Text(value="Begin", size=16),
                )
            ],
        )
        heading_end = ft.Row(
            # spacing=1,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=140, left=200),
                    content=ft.Text(value="End", size=16),
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
        self.gradient_color_holder = ft.Container(
            width=20,
            height=20,
            bgcolor=ft.colors.RED,
            border_radius=5,
            margin=ft.margin.only(left=10),
            on_click=self.open_alert_dlg1,
            # ink=True,
        )
        self.gradient_color_holder1 = ft.Container(
            width=20,
            height=20,
            bgcolor=ft.colors.RED,
            border_radius=5,
            margin=ft.margin.only(left=10),
            on_click=self.open_alert_dlg2,
            # ink=True,
        )

        self.color_picker = ColorPicker(color="#c8df6f", width=300)
        self.color_picker1 = ColorPicker(color="#c8df6f", width=300)
        self.color_picker2 = ColorPicker(color="#c8df6f", width=300)
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
        self.color_picker_modal1 = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=6),
            content=self.color_picker1,
            actions=[
                ft.Container(
                    width=90,
                    height=36,
                    # margin=ft.margin.only(top=130),
                    bgcolor=ft.colors.WHITE30,
                    alignment=ft.alignment.center,
                    border_radius=8,
                    ink=True,
                    on_click=self.close_dlg1,
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
                    on_click=self.use_color_gradient,
                    content=ft.Text("Use Color", size=16),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.color_picker_modal2 = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=6),
            content=self.color_picker2,
            actions=[
                ft.Container(
                    width=90,
                    height=36,
                    # margin=ft.margin.only(top=130),
                    bgcolor=ft.colors.WHITE30,
                    alignment=ft.alignment.center,
                    border_radius=8,
                    ink=True,
                    on_click=self.close_dlg2,
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
                    on_click=self.use_color_gradient1,
                    content=ft.Text("Use Color", size=16),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.gradient_hex_holder = ft.Container(
            content=ft.Text(value="#ff0000", size=16)
        )
        self.gradient_hex_holder1 = ft.Container(
            content=ft.Text(value="#ff0000", size=16)
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

        self.gradient_color_box = ft.Container(
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                # margin=ft.margin.only(left=10, top=290),
                border_radius=7,
                content=ft.Row(
                    controls=[self.gradient_color_holder, self.gradient_hex_holder]
                ),
                margin=ft.margin.only(left=10, top=75),
            )
        )
        self.gradient_color_box1 = ft.Container(
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                # margin=ft.margin.only(left=10, top=290),
                border_radius=7,
                content=ft.Row(
                    controls=[self.gradient_color_holder1, self.gradient_hex_holder1]
                ),
                margin=ft.margin.only(left=10, top=140),
            )
        )

        self.control_name_space = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                # content_padding=ft.padding.only(left=5, right=80),
                # label="Control Name",
                width=380,
                hint_text= "Add Name",
                border= ft.InputBorder.UNDERLINE
            ),
            margin=ft.margin.only(left=10, top=90),
        )
        self.control_rotation = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                # content_padding=ft.padding.only(left=5, right=80),
                label="Rotation",
                width=120,
                height=40,
            ),
            margin=ft.margin.only(left=310, top=10),
        )

        self.control_width = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                # content_padding=ft.padding.only(left=5, right=5),
                hint_text= "Add Width",
                border= ft.InputBorder.UNDERLINE
            ),
            margin=ft.margin.only(left=160, top=185),
        )

        self.gradient = ft.Container(
            margin=ft.margin.only(top=10, left=10),
            content=ft.Dropdown(
                width=170,
                autofocus=False,
                border_color="black",
                border=ft.border.all(color="black", width=1),
                hint_text="Choose Gradient Type",
                options=[
                    ft.dropdown.Option(key="LinearGradient"),
                    ft.dropdown.Option(key="RadialGradient"),
                    ft.dropdown.Option(key="SweepGradient"),
                ],
                on_change=self.on_change,
            ),
        )

        self.choose_begin = ft.Container(
            margin=ft.margin.only(top=60, left=270),
            content=ft.Dropdown(
                width=170,
                autofocus=False,
                border_color="black",
                border=ft.border.all(color="black", width=1),
                hint_text="Choose Begin",
                options=[
                    ft.dropdown.Option(key="center"),
                    ft.dropdown.Option(key="center_left"),
                    ft.dropdown.Option(key="center_right"),
                    ft.dropdown.Option(key="bottom_center"),
                    ft.dropdown.Option(key="bottom_left"),
                    ft.dropdown.Option(key="bottom_right"),
                    ft.dropdown.Option(key="top_center"),
                    ft.dropdown.Option(key="top_right"),
                    ft.dropdown.Option(key="top_left"),
                ],
                on_change=self.on_change,
            ),
        )
        self.choose_end = ft.Container(
            margin=ft.margin.only(top=140, left=270),
            content=ft.Dropdown(
                width=170,
                autofocus=False,
                border_color="black",
                border=ft.border.all(color="black", width=1),
                hint_text="Choose End",
                options=[
                    ft.dropdown.Option(key="center"),
                    ft.dropdown.Option(key="center_left"),
                    ft.dropdown.Option(key="center_right"),
                    ft.dropdown.Option(key="bottom_center"),
                    ft.dropdown.Option(key="bottom_left"),
                    ft.dropdown.Option(key="bottom_right"),
                    ft.dropdown.Option(key="top_center"),
                    ft.dropdown.Option(key="top_right"),
                    ft.dropdown.Option(key="top_left"),
                ],
                on_change=self.on_change,
            ),
        )

        # print(self.gradient.content.options[1])

        self.control_opacity = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                # content_padding=ft.padding.only(left=5, right=5),
                hint_text= "Add Opacity",
                border= ft.InputBorder.UNDERLINE
            ),
            margin=ft.margin.only(left=310, top=185),
        )

        ft.Column()

        self.control_height = ft.Container(
            content=ft.Container(
                # width=140,
                content=ft.TextField(
                    # text_align=ft.alignment.center,
                    width=140,
                    # content_padding=ft.padding.only(left=5, right=15, top=30),
                    hint_text= "Add Height",
                    border= ft.InputBorder.UNDERLINE
                ),
            ),
            margin=ft.margin.only(left=15, top=185),
        )
        self.cover_component = ft.Container(
            width=460,
            border=ft.border.all(width=2, color="cyan"),
            height=400,
            margin=ft.margin.only(bottom=480, top=350),
            content=ft.Column(
                controls=[
                    ft.Stack(
                        controls=[
                            self.gradient_color_box1,
                            self.gradient_color_box,
                            self.choose_begin,
                            self.choose_end,
                            self.control_rotation,
                            self.gradient,
                            heading_end,
                            heading_beign,
                        ]
                    )
                ],
                scroll="always",
            ),
            border_radius=5,
        )

        heading_opacity = ft.Container(
            margin=ft.margin.only(left=310, top=155),
            content=ft.Row(
                controls=[
                    ft.Text(value="Opacity", size=15),
                ]
            ),
        )

        self.propertiesColumn.controls[0].controls = [
            heading,
            heading_width,
            self.control_name_space,
            self.control_width,
            heading_Control_name,
            heading_height,
            self.color_box,
            self.control_height,
            heading_color,
            heading_opacity,
            self.control_opacity,
            heading_gradient,
            self.cover_component,
        ]

        self.propertiesContainer.content = self.propertiesColumn

        return self.propertiesContainer


def init_process():
    # Code to initialize each process if needed
    pass


def build_and_run(page):
    properties_toolbar = PropertiesToolbar(page)
    properties_container = properties_toolbar.build()

    # Additional code to set up the rest of your application

    # ft.run(page)


if __name__ == "__main__":
    # Create a multiprocessing.Pool
    with multiprocessing.Pool(
        processes=multiprocessing.cpu_count(), initializer=init_process
    ) as pool:
        # Create a page for each process
        pages = [ft.Page() for _ in range(pool._processes)]

        # Use multiprocessing.Pool to run the build_and_run function for each process
        pool.map(build_and_run, pages)
