import multiprocessing
import flet as ft
from ..ColorPicker.color_picker import ColorPicker

# ft.Dis


# ft.SweepGradient()
ft.Container()


class PropertiesToolbar(ft.UserControl):
    def __init__(self, page, manager):
        self.page = page
        super().__init__()
        self.imanager = manager
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

    def change(self, e: ft.ControlEvent, prop):
        # add code to check and not allow for alphabets and soon
        self.imanager.change_property(prop, e.control.value)

    def build(self):
        # (existing build code)

        self.propertiesContainer = ft.Container(
            height=1200,
            bgcolor=ft.colors.with_opacity(opacity=0.6, color=ft.colors.BLACK45),
            border_radius=ft.border_radius.all(15),
        )

        self.propertiesColumn = ft.Column(scroll="always")

        heading = ft.Container(
            margin=ft.margin.only(top=10),
            alignment=ft.alignment.center,
            content=ft.Text(value="Properties", size=20),
        )
        
        # tight=True,
        # spacing=1,
        heading_beign = ft.Container( # Be more specific 
            margin=ft.margin.all(10),
            content=ft.Text(value="Begin", size=15),
            )
        heading_end = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Text(value="End", size=15),
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

        self.control_rotation = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                label="Rotation",
                width=120,
                height=40,
            ),
        )
 
        self.gradient = ft.Container(
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

        
        ft.Column()

        self.control_name_space = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                hint_text= "Add Name",
                border= ft.InputBorder.UNDERLINE
            ),
        )
        self.control_width = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text= "Add Width",
                border= ft.InputBorder.UNDERLINE,
                on_change= lambda e: self.change(e, "-w")
            ),
        )
        self.control_height = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text= "Add Height",
                border= ft.InputBorder.UNDERLINE,
                on_change= lambda e: self.change(e, "-h")
            ),
        )
        self.control_opacity = ft.Container(
            content=ft.TextField(
                text_align=ft.alignment.center,
                width=140,
                hint_text= "Add Opacity",
                border= ft.InputBorder.UNDERLINE,
                # ,
                on_change= lambda e: self.change(e, "-o")
            ),
        )
        self.color_box = ft.Container( # why does it have two containers
            content=ft.Container(
                width=140,
                height=30,
                bgcolor=ft.colors.GREY_800,
                border_radius=7,
                content=ft.Row(controls=[self.color_holder, self.hex_holder]),
            )
        )
        self.cover_component = ft.Container(
            width=460,
            border=ft.border.all(width=2, color="cyan"),
            height=400,
            padding= ft.padding.all(10),
            content=ft.Column(
                spacing= 0,
                controls=[
                    ft.Row(
                        wrap= True,
                        controls=[
                            self.gradient,
                            self.control_rotation,
                        ],
                        alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    heading_beign, # Be more specific with the naming
                    ft.Row(
                        wrap= True,
                        controls=[
                            self.gradient_color_box,
                            self.choose_begin,
                            
                        ]
                    ),
                    heading_end,
                    ft.Row(
                        wrap= True,
                        controls=[
                            self.gradient_color_box1,
                            self.choose_end,
                            
                        ]
                    )
                ],
                scroll="always",
            ),
            border_radius=5,
        )
        
        heading_Control_name = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing= 0,
                controls=[
                    ft.Text(value="Control Name", size=15),
                    self.control_name_space,
                ]
            ),
        )
        
        heading_width = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing= 0,
                controls=[
                    ft.Text(value="Width", size=15),
                    self.control_width,
                ]
            ),
        )
        heading_height = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing= 0,
                controls=[
                    ft.Text(value="Height", size=15),
                    self.control_height,
                ]
            ),
        )
        heading_opacity = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing= 0,
                controls=[
                    ft.Text(value="Opacity", size=15),
                    self.control_opacity,
                ]
            ),
        )
        
        heading_color = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing= 5,
                controls=[
                    ft.Text(value="Color", size=15),
                    self.color_box,
                ]
            ),
        )
        heading_gradient = ft.Container(
            margin=ft.margin.all(10),
            content=ft.Column(
                spacing= 5,
                controls=[
                    ft.Text(value="Gradient", size=15),
                    self.cover_component,
                ]
            ),
        )
        
        # can use a for loop instead to reduce redundancy
        heading_grid = ft.GridView(
            max_extent= 150,
            child_aspect_ratio= 1.5,
            controls=[
                heading_height,
                heading_width,
                heading_opacity,
            ]
        )

        self.propertiesColumn.controls = [
            heading,
            heading_Control_name,
            heading_grid,
            heading_color,
            heading_gradient,
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