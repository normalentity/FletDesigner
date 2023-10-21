import flet as ft
import json


class Parser:
    def __init__(self, jsonfilepath=None):
        if jsonfilepath:
            with open(jsonfilepath) as f:
                self.json = json.load(f)
        self.keys = {}

    def update_properties(self, key, val):
        self.keys[f"{key}"].width = val["width"]
        self.keys[f"{key}"].height = val["height"]
        self.keys[f"{key}"].expand = val["expand"]
        self.keys[f"{key}"].opacity = val["opacity"]
        self.keys[f"{key}"].bgcolor = val["bgcolor"]

    def parse(self):
        for item in self.json:
            for key, val in item.items():
                if val["type"] == "Container":
                    self.keys[f"{key}"] = ft.Container()
                    self.update_properties(key, val)
                    # Add the properties of self.c1
                    self.keys[f"{key}"].border_radius = ft.border_radius.all(
                        val["border_radius"]
                    )
                    self.keys[f"{key}"].content = ft.Row()
                    
                if val["type"] == "IconButton":
                    self.keys[f"{key}"] = ft.TextButton()
                    self.update_properties(key, val)
                    self.keys[f"{key}"].icon = ft.icons.COFFEE
                    self.keys[f"{key}"].text = val["text"]
                    self.keys[f"c1"].content.controls.append(self.keys[f"{key}"])

