import flet as ft
from Designer import DesignerSection
from UI.Toolbar import Toolbar
from UI.ToolbarItem import ToolbarItem
from UI.ToolbarItems import ToolbarItems
from UI.Properties_Toolbar import PropertiesToolbar


class DesignPage(
    ft.View,
):
    def __init__(self, page):
        self.page = page
        super().__init__()

    def build(self):
        self.route = "/design"
        self.bgcolor = "#131313"
        self.designsection = DesignerSection()
        Container = ToolbarItem(text="Container", widget="Container")
        Row = ToolbarItem(text="Row", widget="Row")
        Column = ToolbarItem(text="Column", widget="Column")
        Text = ToolbarItem(text="Text", widget="Text")
        property_toolbar = PropertiesToolbar(page=self.page)

        # placeholderbuttons

        itemslist = [Container, Row, Column, Text]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems)
        self.displayarea = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection, property_toolbar],
            height=1700,
        )
        self.controls.append(self.displayarea)
        return self
