import flet as ft

from ..ColorPicker.color_picker import ColorPicker


class BasePropertiesToolbar(ft.UserControl):
    def __init__(self, page, manager, parser_engine):
        self.page = page
        self.object_controller = None
        self.imanager = manager
        self.control_height = None
        self.parser_engine = parser_engine
        super().__init__(self.parser_engine)
        self.expand = int((1 + 0.2) * 5)

        # Define the common properties here
        self.control_name_space = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                hint_text="Add Name",
                border=ft.InputBorder.UNDERLINE,
                on_change=lambda e: self.change(e, "-ctrlname"),
            ),
        )
        self.control_width = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text="Add Width",
                border=ft.InputBorder.UNDERLINE,
                on_change=lambda e: self.change(e, "-w"),
            ),
        )
        self.control_height = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text="Add Height",
                border=ft.InputBorder.UNDERLINE,
                on_change=lambda e: self.change(e, "-h"),
            ),
        )
        self.control_opacity = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text="Add Opacity",
                border=ft.InputBorder.UNDERLINE,
                on_change=lambda e: self.change(e, "-o"),
            ),
        )

        # Define the headings
        self.heading_Control_name = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(value="Control Name", size=15),
                    self.control_name_space,
                ],
            ),
        )
        self.heading_width = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(value="Width", size=15),
                    self.control_width,
                ],
            ),
        )

        self.DeleteButton = ft.Container(
            width=500,
            visible=True,
            # animate=ft.animation.Animation("400", "decelerate"),
            # animate_positio=200,
            alignment=ft.alignment.center,
            height=39,
            margin=ft.margin.only(top=400),
            content=ft.Column(
                horizontal_alignment="center",
                controls=[
                    ft.ElevatedButton(
                        color=ft.colors.BLACK54,
                        text="Delete",
                        width=150,
                        height=39,
                        on_click=self.Delete,
                    )
                ],
            ),
        )

        self.heading_height = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(value="Height", size=15),
                    self.control_height,
                ],
            ),
        )
        self.heading_opacity = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(value="Opacity", size=15),
                    self.control_opacity,
                ],
            ),
        )

        # Define the main holder
        self.propertiesContainer = ft.Container(
            height=1200,
            bgcolor=ft.colors.with_opacity(opacity=0.6, color=ft.colors.BLACK45),
            border_radius=ft.border_radius.all(15),
            visible=False,
        )
        self.propertiesColumn = ft.Column(scroll="always")
        heading = ft.Container(
            margin=ft.margin.only(top=10),
            alignment=ft.alignment.center,
            content=ft.Text(value="Properties", size=20),
        )

        # Add the headings to the grid view
        heading_grid = ft.GridView(
            max_extent=150,
            child_aspect_ratio=1.5,
            controls=[
                self.heading_height,
                self.heading_width,
                self.heading_opacity,
            ],
        )

        # Add the grid view and headings to the column
        self.propertiesColumn.controls = [
            heading,
            self.heading_Control_name,
            heading_grid,
        ]

        # Add the column to the container
        self.propertiesContainer.content = self.propertiesColumn

    def build(self):
        return self.propertiesContainer

    def change(self, e: ft.ControlEvent, prop):
        # add code to check and not allow for alphabets and soon
        self.imanager.change_property(prop=prop, value=e.control.value)

    def open_alert_dlg(self, e):
        self.page.dialog = self.color_picker_modal
        self.color_picker_modal.open = True
        self.page.update()

    def close_dlg(self, e):
        self.color_picker_modal.open = False
        self.page.update()

    def use_color(self, e):
        self.color_holder.bgcolor = self.color_picker.color
        self.hex_holder.content.value = self.color_picker.color
        self.imanager.change_property(prop="-c", value=self.color_picker.color)
        self.color_holder.update()
        self.hex_holder.content.update()
        # self.color_picker_modal.open = False
        self.color_holder.update()
        self.page.update()

    def Delete(self, e):
        self.imanager.change_property(
            prop="-del",
        )


class ContainerPropertiesToolbar(BasePropertiesToolbar):
    def __init__(self, page, manager, parser_engine):
        super().__init__(page, manager, parser_engine)

        # Define the specific properties for Container
        self.control_border_radius = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text="Border Radius",
                border=ft.InputBorder.UNDERLINE,
                on_change=lambda e: self.change(e, "-b"),
            ),
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

        # Define the heading for the control
        self.heading_border_radius = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Text(value="Border Radius", size=15),
                    self.control_border_radius,
                ],
            ),
        )
        self.control_rotation = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                label="Rotation",
                width=120,
                height=40,
                on_change=self.change_rotation,
            ),
        )

        self.heading_beign = ft.Container(  # Be more specific
            margin=ft.margin.all(10),
            content=ft.Text(value="Begin", size=15),
        )
        self.heading_end = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Text(value="End", size=15),
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

        self.color_picker = ColorPicker(color="#c8df6f", width=290)

        self.color_picker1 = ColorPicker(color="#c8df6f", width=300)
        self.color_picker2 = ColorPicker(color="#c8df6f", width=300)
        self.color_picker_modal = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=6),
            content=self.color_picker,
            modal=False,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
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

        self.gradient_color_box = ft.Container(
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                border_radius=7,
                content=ft.Row(
                    controls=[self.gradient_color_holder, self.gradient_hex_holder]
                ),
            )
        )
        self.gradient_color_box1 = ft.Container(
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                border_radius=7,
                content=ft.Row(
                    controls=[self.gradient_color_holder1, self.gradient_hex_holder1]
                ),
            )
        )

        self.color_box = ft.Container(  # why does it have two containers
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                border_radius=7,
                content=ft.Row(controls=[self.color_holder, self.hex_holder]),
            )
        )

        self.gradient = ft.Container(
            content=ft.Dropdown(
                width=170,
                autofocus=False,
                value="LinearGradient",
                border_color="black",
                border=ft.border.all(color="black", width=1),
                hint_text="Choose Gradient Type",
                options=[
                    ft.dropdown.Option(key="LinearGradient"),
                    ft.dropdown.Option(key="RadialGradient"),
                    ft.dropdown.Option(key="SweepGradient"),
                ],
                # on_change=self.on_change,
            ),
        )

        self.choose_begin = ft.Container(
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
                on_change=self.on_change_begin,
            ),
        )
        self.choose_end = ft.Container(
            content=ft.Dropdown(
                width=170,
                autofocus=False,
                value="top_left",
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
                on_change=self.on_change_end,
            ),
        )

        self.cover_component = ft.Container(
            width=460,
            visible=False,
            animate=ft.animation.Animation(
                duration=10, curve=ft.animation.AnimationCurve.DECELERATE
            ),
            animate_opacity=200,
            border=ft.border.all(width=2, color="cyan"),
            height=400,
            padding=ft.padding.all(10),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Row(
                        wrap=True,
                        controls=[
                            self.gradient,
                            self.control_rotation,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.heading_beign,  # Be more specific with the naming
                    ft.Row(
                        wrap=True,
                        controls=[
                            self.gradient_color_box,
                            self.choose_begin,
                        ],
                    ),
                    self.heading_end,
                    ft.Row(
                        wrap=True,
                        controls=[
                            self.gradient_color_box1,
                            self.choose_end,
                        ],
                    ),
                ],
                scroll="always",
            ),
            border_radius=5,
        )

        self.gradient_switch = ft.Container(
            # width=690,
            # margin=ft.margin.only(top=2, left=160),
            content=ft.Switch(
                thumb_color=ft.colors.BLUE_100,
                on_change=self.change_visibilty_gradient,
                track_color=ft.colors.BLACK,
            ),
        )
        self.heading_gradient = ft.Container(
            margin=ft.margin.only(top=6),
            content=ft.Column(
                spacing=4,
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                spacing=3,
                                controls=[
                                    ft.Text(value="Gradient", size=15),
                                    self.gradient_switch,
                                ],
                            )
                        ]
                    ),
                    self.cover_component,
                ],
            ),
        )

        self.heading_color = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Text(value="Color", size=15),
                    self.color_box,
                ],
            ),
        )

        # Add the new control and its heading to the column
        self.propertiesColumn.controls.extend(
            [
                self.heading_color,
                self.heading_border_radius,
                self.heading_gradient,
                self.DeleteButton,
            ]
        )

    def on_change_begin(self, e, control_name=None):
        self.selection_value = e.control.value

        if self.selection_value == "top_left":
            self.selection_value = ft.alignment.top_left
        if self.selection_value == "top_center":
            self.selection_value = ft.alignment.top_center
        if self.selection_value == "top_right":
            self.selection_value = ft.alignment.top_right
        if self.selection_value == "bottom_left":
            self.selection_value = ft.alignment.bottom_left
        if self.selection_value == "bottom_center":
            self.selection_value = ft.alignment.bottom_center
        if self.selection_value == "bottom_right":
            self.selection_value = ft.alignment.bottom_right
        if self.selection_value == "center_left":
            self.selection_value = ft.alignment.center_left
        if self.selection_value == "center_right":
            self.selection_value = ft.alignment.center_right
        if self.selection_value == "center":
            self.selection_value = ft.alignment.center
        self.imanager.change_property(
            prop="-change_begin",
            begin=self.selection_value,
        )

    def on_change_end(self, e, control_name=None):
        self.selection_value = e.control.value
        if self.selection_value == "top_left":
            self.selection_value = ft.alignment.top_left
        if self.selection_value == "top_center":
            self.selection_value = ft.alignment.top_center
        if self.selection_value == "top_right":
            self.selection_value = ft.alignment.top_right
        if self.selection_value == "bottom_left":
            self.selection_value = ft.alignment.bottom_left
        if self.selection_value == "bottom_center":
            self.selection_value = ft.alignment.bottom_center
        if self.selection_value == "bottom_right":
            self.selection_value = ft.alignment.bottom_right
        if self.selection_value == "center_left":
            self.selection_value = ft.alignment.center_left
        if self.selection_value == "center_right":
            self.selection_value = ft.alignment.center_right
        if self.selection_value == "center":
            self.selection_value = ft.alignment.center

        self.imanager.change_property(
            prop="-change_end",
            end=self.selection_value,
        )

    def use_color_gradient(self, e):
        self.gradient_color_holder.bgcolor = self.color_picker1.color
        self.gradient_hex_holder.content.value = self.color_picker1.color
        self.imanager.change_property(prop="-gc", value=self.color_picker1.color)
        self.gradient_color_holder.update()
        self.gradient_hex_holder.content.update()
        self.color_picker_modal1.open = False
        self.gradient_color_holder.update()
        self.page.update()

    def change_rotation(self, e):
        self.rotation = e.control.value
        self.imanager.change_property(
            prop="-rotation",
            rotation=self.rotation,
        )

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
        self.imanager.change_property(prop="-c", value=self.color_picker.color)
        self.color_holder.update()
        self.hex_holder.content.update()
        # self.color_picker_modal.open = False
        self.color_holder.update()
        self.page.update()

    def use_color_gradient1(self, e):
        self.gradient_color_holder1.bgcolor = self.color_picker2.color
        self.gradient_hex_holder1.content.value = self.color_picker2.color
        self.imanager.change_property(
            prop="-gc", value_gradient=self.color_picker2.color
        )

        self.gradient_color_holder1.update()
        self.gradient_hex_holder1.content.update()
        self.color_picker_modal2.open = False
        self.gradient_color_holder1.update()
        self.page.update()

    def change_visibilty_gradient(self, e, value=None):
        if self.gradient_switch.content.value == True:
            self.imanager.change_property(prop="-gc")
            self.cover_component.visible = True
            # self.DeleteButton.margin = ft.margin.only(top=200)
        elif self.gradient_switch.content.value == False:
            self.imanager.change_property(prop="-gcr")
            self.cover_component.visible = False
        self.page.update()
        self.cover_component.update()

    def close_dlg1(self, e):
        self.color_picker_modal1.open = False
        self.page.update()

    def close_dlg2(self, e):
        self.color_picker_modal2.open = False
        self.page.update()


class ElevatedButtonPropertiesToolbar(BasePropertiesToolbar):
    def __init__(self, page, manager, parser_engine):
        super().__init__(page, manager, parser_engine)

        # Define the heading for the control
        self.control_text = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text="Text",
                border=ft.InputBorder.UNDERLINE,
                on_change=lambda e: self.change(e, "-t"),
            ),
        )

        self.color_picker = ColorPicker(color="#c8df6f", width=290)

        self.hex_holder = ft.Container(content=ft.Text(value="#ff0000", size=16))
        self.color_holder = ft.Container(
            width=20,
            height=20,
            bgcolor=ft.colors.RED,
            border_radius=5,
            margin=ft.margin.only(left=10),
            on_click=self.open_alert_dlg,
            # ink=True,
        )

        self.color_picker_modal = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=6),
            content=self.color_picker,
            modal=False,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
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

        self.color_box = ft.Container(  # why does it have two containers
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                border_radius=7,
                content=ft.Row(controls=[self.color_holder, self.hex_holder]),
            )
        )
        self.heading_text = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Text(value="Text", size=15),
                    self.control_text,
                ],
            ),
        )

        self.heading_color = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Text(value="Color", size=15),
                    self.color_box,
                ],
            ),
        )

        self.propertiesColumn.controls.extend(
            [self.heading_text, self.heading_color, self.DeleteButton]
        )
