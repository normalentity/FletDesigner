from math import pi
from typing import Optional

from flet import Container, Control, Row, Text, padding


class MenuButton(Container):
    def __init__(
        self, title: str, icon: Optional[Control] = None, selected: bool = False
    ):
        super().__init__()
        self.icon = icon
        self.title = title
        self._selected = selected
        self.padding = padding.only(left=43)
        self.height = 38
        self.border_radius = 4
        self.ink = True
        self.on_click = self.item_click

    def item_click(self, _):
        pass

    def _build(self):
        row = Row()
        if self.icon != None:
            row.controls.append(self.icon)
        row.controls.append(Text(self.title))
        self.content = row

    def _before_build_command(self):
        self.bgcolor = "surfacevariant" if self._selected else None
        super()._before_build_command()