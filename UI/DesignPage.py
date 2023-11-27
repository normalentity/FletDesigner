import flet as ft
from UI.Designer import DesignerSection
from UI.Toolbar import Toolbar
from UI.ToolbarItem import ToolbarItem
from UI.ToolbarItems import ToolbarItems
from UI.Properties_Toolbar import PropertiesToolbar
from UI.Interactve_manager import IManager


class DesignPage(
    ft.View,
):
    def __init__(self):
        self.manager = IManager()
        super().__init__()
        self.expand = True

    def build(self):
        self.route = "/design"
        self.bgcolor = "#131313"
        self.designsection = DesignerSection(self.manager)
        Container = ToolbarItem(text="Container", widget="Container")
        Row = ToolbarItem(text="Row", widget="Row")
        Column = ToolbarItem(text="Column", widget="Column")
        Text = ToolbarItem(text="Text", widget="Text")
        TextButton = ToolbarItem(text="ElevatedButton", widget="Text")
        property_toolbar = PropertiesToolbar(
            page=self.page,
        )
        self.manager.detail = property_toolbar

        # placeholderbuttons

        itemslist = [Container, Row, Column, Text, TextButton]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems, )#self.window_width)
        self.displayarea = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection, property_toolbar],
            height=1400,
        )
        self.controls.append(self.displayarea)
        return self
