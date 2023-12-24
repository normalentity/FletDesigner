import flet as ft
from ..UI.Designer import DesignerSection
from ..UI.Toolbar import Toolbar
from ..UI.ToolbarItem import ToolbarItem
from ..UI.ToolbarItems import ToolbarItems
from ..UI.Properties_Toolbar import ContainerPropertiesToolbar, BasePropertiesToolbar
from .Interactive_Manager import IManager
from ..Parser.parser import ParserEngine


class DesignPage(ft.View):
    """The Main Page that manages the Layout."""

    def __init__(self, project_file_path: str, page):
        self.page = page
        self.project_file_path = project_file_path
        self.parser_engine = ParserEngine(file_path=self.project_file_path)
        self.manager = IManager(parser_engine=self.parser_engine)
        self.detail: ContainerPropertiesToolbar = self.manager.detail
        self.manager.page = self.page
        self.parser_engine.manager = self.manager
        # self.elevatedbar = ElevatedButton(page=self.page)
        super().__init__()
        self.expand = True

    def update_displayarea(self):
        # Remove the old detail from displayarea
        self.displayarea.controls.remove(self.detail)

        # Update self.detail
        self.detail = self.manager.detail

        # Add the new detail to displayarea
        self.displayarea.controls.append(self.detail)

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
        # self.manager.detail: ContainerPropertiesToolbar = self.detail
        self.manager.object_controller: DesignerSection = self.designsection
        self.manager.eb = self
        # self.manager.eb: ElevatedButton = self.elevatedbar
        # self.parser_engine.properties_class.gradient_switch: PropertiesToolbar

        # placeholderbuttons
        itemslist = [Container, Row, Column, Text, TextButton]
        toolbaritems = ToolbarItems(itemslist)
        self.toolbar = Toolbar(toolbaritems)
        self.displayarea = ft.Row(
            expand=True,
            controls=[self.toolbar, self.designsection, self.detail],
            height=1400,
        )
        self.controls.append(self.displayarea)
        return self
