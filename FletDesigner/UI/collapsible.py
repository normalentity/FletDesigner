from math import pi
from typing import Optional

from flet import Column, Container, Control, Icon, Row, Text, icons, padding


class Collapsible(Column):
    def __init__(
        self,
        title: str,
        content: Control,
        icon: Optional[Control] = None,
        spacing: float = 3,
    ):
        super().__init__()
        self.icon = icon
        self.title = title
        self.shevron = Icon(
            icons.KEYBOARD_ARROW_DOWN_ROUNDED,
            animate_rotation=100,
            rotate=0,
        )
        self.content = Column(
            [Container(height=spacing), content],
            height=0,
            spacing=0,
            animate_size=100,
            opacity=0,
            animate_opacity=100,
        )
        self.spacing = 0

    def header_click(self, e):
        self.content.height = None if self.content.height == 0 else 0
        self.content.opacity = 0 if self.content.height == 0 else 1
        self.shevron.rotate = pi if self.shevron.rotate == 0 else 0
        self.update()

    def _build(self):
        title_row = Row()
        if self.icon != None:
            title_row.controls.append(self.icon)
        title_row.controls.append(Text(self.title))
        self.controls.extend(
            [
                Container(
                    Row([title_row, self.shevron], alignment="spaceBetween"),
                    padding=padding.only(left=8, right=8),
                    height=38,
                    border_radius=4,
                    ink=True,
                    on_click=self.header_click,
                ),
                self.content,
            ]
        )