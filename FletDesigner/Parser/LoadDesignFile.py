import json
import flet as ft
from .Initialize_Control import Parser
import typing


class LoadDesignFile:
    def __init__(
        self,
        jsonfilepath: str,
    ):
        self.__jsonfilepath = jsonfilepath
        self.__parser = Parser(jsonfilepath=self.__jsonfilepath)
        self.__parser.parse()
        self.__keys = self.__parser.keys

    def __getattr__(self, name: str):
        try:
            return self.__keys[f"{name}"]
        except Exception as e:
            print(f"There is no widget named '{name}")

    def __setattr__(self, name, value):
        # print(name[0:17])
        if name[0:17] == "_LoadDesignFile__":
            # print("hi")
            super().__setattr__(name, value)
        else:
            self.__keys[f"{name}"] = value

    def run(self):
        ft.app(target=self.ConstructPage)

    def ConstructPage(self, page: ft.Page):
        # Initialization of the page
        self.__page = page
        for control in self.__keys.values():
            if not control.__dict__.get("isChild"):
                self.__page.add(control)
        page.window_height = 800
        # page.theme = ft.theme.Theme(color_scheme_seed="cyan100")
        page.update()
        page.window_width = 800
