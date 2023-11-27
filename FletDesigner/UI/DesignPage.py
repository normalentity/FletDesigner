import flet as ft
from ..UI.Designer import DesignerSection
from ..UI.Toolbar import Toolbar
from ..UI.ToolbarItem import ToolbarItem
from ..UI.ToolbarItems import ToolbarItems
from ..UI.Properties_Toolbar import PropertiesToolbar


class DesignPage(
    ft.View,
):
    def __init__(self, window_width1):
        self.window_width = window_width1
        print(self.window_width)
        super().__init__()

    def build(self):
        self.route = "/design"
        self.bgcolor = "#131313"
        self.designsection = DesignerSection(self.window_width)
        Container = ToolbarItem(text="Container", widget="Container")
        Row = ToolbarItem(text="Row", widget="Row")
        Column = ToolbarItem(text="Column", widget="Column")
        Text = ToolbarItem(text="Text", widget="Text")
        TextButton = ToolbarItem(text="ElevatedButton", widget="Text")
        property_toolbar = PropertiesToolbar(
            page=self.page, window_width=self.window_width
        )

        # placeholderbuttons

        itemslist = [Container, Row, Column, Text, TextButton]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems, self.window_width)
        self.displayarea = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection, property_toolbar],
            height=1400,
        )
        self.controls.append(self.displayarea)
        return self
