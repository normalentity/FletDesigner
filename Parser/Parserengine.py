import flet as ft
import json
from .initialize_control import Initialize_Component


class Parser:
    def __init__(self, jsonfilepath=None):
        if jsonfilepath:
            with open(jsonfilepath) as f:
                self.json = json.load(f)
        self.keys = {}

    def parse(self):
        for item in self.json:
            for key, val in item.items():
                if val["type"] == "Container":
                    Initialize_Component(self, key, val)
                if val["type"] == "IconButton":
                    Initialize_Component(self, key, val)
                    self.keys[f"c1"].content.controls.append(self.keys[f"{key}"])

    def Add_Widgetds(self, Control):
        pass
