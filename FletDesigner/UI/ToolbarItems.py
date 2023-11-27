import flet as ft
from ..UI.ToolbarItem import ToolbarItem


class ToolbarItems(ft.UserControl):
    def __init__(self, ToolbarItemList: list):
        self.toolbaritemlist = ToolbarItemList
        self.selected = None
        super().__init__()

    def set_selected(self, container: ft.Container):
        container.border = ft.border.all(3, ft.colors.RED_100)
        container.update()
        self.update()

    def unset_selected(self, container: ft.Container):
        container.border = None
        container.update()
        self.update()

    def selectionchanged(self, event):
        if self.selected:
            self.unset_selected(self.selected)
        self.selected = event.control
        self.set_selected(self.selected)

    def build(self):
        self.column = ft.Column(
            scroll="always",
            horizontal_alignment="center",
            controls=[],
        )
        for item in self.toolbaritemlist:
            item.add_selectionchanged_callback(self.selectionchanged)
            self.column.controls.append(item)
        return self.column

    def add(self, item):
        self.column.controls.append(item)
        self.column.update()
