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
                            title=ft.ElevatedButton(
                                width=200, height=200, bgcolor="red"
                            ),
                        ),
                    ],
                )
            ],
        ),
        padding=ft.padding.symmetric(vertical=10),
    )

    page.add(template)


ft.app(target=main)
