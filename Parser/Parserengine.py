import flet as ft
import json
from .initialize_control import Initialize_Components


class Parser:
    def __init__(self, jsonfilepath=None):
        if jsonfilepath:
            with open(jsonfilepath) as f:
                self.json = json.load(f)
        # to store all the control names for the user to access
        self.keys = {}

    def parse(self):
        for item in self.json:
            for key, val in item.items():
                # the val and the key variables are the keys and values we retrieve from the json file
                Initialize_Components(self, key, val)

    def Add_Widgets(self, Control):
        pass
