import flet as ft
from Designer import DesignerSection
from UI.Toolbar import Toolbar
from UI.ToolbarItem import ToolbarItem
from UI.ToolbarItems import ToolbarItems


class DesignPage(ft.View):
    def __init__(self):
        super().__init__()

    def build(self):
        self.route = "/design"
        self.bgcolor = "#131313"
        self.designsection = DesignerSection()
        Container = ToolbarItem(text="Container", widget="Container")
        Row = ToolbarItem(text="Row", widget="Row")
        # placeholderbuttons

        itemslist = [
            Container,
            Row,
        ]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems)
        self.sm = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection],
            height=1700,
        )
        self.controls.append(self.sm)
        return self
