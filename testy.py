import flet as ft


def main(page: ft.Page):
    page.title = "ListTile Examples"

    
    template = ft.Container(
        expand=False,
        width=450,
        height=500,
        content=ft.Column(
            width=10,
            expand=False,
            controls=[
                ft.ListView(
                    # width=300,
                    # height=400,
                    # divider_thickness=2,
                    controls=[
                        ft.ListTile(
                            title=ft.Text(value="Styling", size=17),
                        ),
                        ft.ListTile(
                            expand=False,
                            width=20,
                            # height=40,
                            title=ft.Container(
                                width=10,
                                height=70,
                                expand=False,
                                content=ft.TextField(
                                    # text_align=ft.alignment.center,
                                    width=20,
                                    height=40,
                                    # content_padding=ft.padding.only(left=5, right=5),
                                    label="Styling",
                                    expand=False,
                                ),
                            )
                            # leading=ft.Container(
                            #     width=20, height=30, margin=ft.margin.only(left=1)
                            # ),
                        ),
                    ],
                )
            ],
        ),
        padding=ft.padding.symmetric(vertical=10),
    )

    page.add(template)


ft.app(target=main)
