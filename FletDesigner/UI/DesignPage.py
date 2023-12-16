import flet as ft
from ..UI.Designer import DesignerSection
from ..UI.Toolbar import Toolbar
from ..UI.ToolbarItem import ToolbarItem
from ..UI.ToolbarItems import ToolbarItems
from ..UI.Properties_Toolbar import PropertiesToolbar
from .Interactive_Manager import IManager
from ..Parser.parser import ParserEngine


class DesignPage(ft.View):
    """The Main Page that manages the Layout."""

    def __init__(self, project_file_path: str, page):
        self.page = page
        self.project_file_path = project_file_path
        self.parser_engine = ParserEngine(file_path=self.project_file_path)
        self.manager = IManager(parser_engine=self.parser_engine)
        self.parser_engine.manager = self.manager
        self.property_toolbar: PropertiesToolbar = PropertiesToolbar(
            self.page, self.manager, parser_engine=self.parser_engine
        )
        super().__init__()
        self.expand = True

    def build(self):
        self.route = "/design"
        self.bgcolor = "#131313"

        self.designsection = DesignerSection(
            self.manager,
            project_file_path=self.project_file_path,
            parser_engine=self.parser_engine,
        )
        Container = ToolbarItem(text="Container", widget="Container")
        Row = ToolbarItem(text="Row", widget="Row")
        Column = ToolbarItem(text="Column", widget="Column")
        Text = ToolbarItem(text="Text", widget="Text")
        TextButton = ToolbarItem(text="ElevatedButton", widget="Text")
        self.manager.detail: PropertiesToolbar = self.property_toolbar
        self.manager.object_controller: DesignerSection = self.designsection
        # self.parser_engine.properties_class.gradient_switch: PropertiesToolbar

        # placeholderbuttons
        itemslist = [Container, Row, Column, Text, TextButton]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems)
        self.displayarea = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection, self.property_toolbar],
            height=1400,
        )
        self.controls.append(self.displayarea)
        return self
