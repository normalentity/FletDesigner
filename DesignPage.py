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
        self.bgcolor = '#131313'
        self.designsection = DesignerSection()
        Container = ToolbarItem("Container")
        Row = ToolbarItem("Row")

        # placeholderbuttons 
        x1 = ToolbarItem("x1")
        x2 = ToolbarItem("x2")
        x3 = ToolbarItem("x3")
        x4 = ToolbarItem("x4")
        x5 = ToolbarItem("x5")

        itemslist = [Container, Row,x1,x2,x3,x4,x5]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems)
        self.sm = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection],
            height=1700,
        )
        self.controls.append(self.sm)
        return self
