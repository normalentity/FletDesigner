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
        self.bgcolor = ft.colors.BLACK
        self.designsection = DesignerSection()
        Container = ToolbarItem("Container")
        Row = ToolbarItem("Row")
        itemslist = [Container, Row]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems)
        self.sm = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection],
            height=1700,
        )
        self.controls.append(self.sm)
        return self
