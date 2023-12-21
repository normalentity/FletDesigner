import flet as ft
import json

# from .initialize_control import Initialize_Components


class Parser:
    def __init__(self, jsonfilepath=None):
        if jsonfilepath:
            with open(jsonfilepath) as f:
                self.json = json.load(f)
        # to store all the control names for the user to access
        self.keys = {}

    def Initialize_Components(self, key, val, parent=None):
        if val["control_type"] == "Container":
            # self.keys[f"{key}"] = ft.Container()
            del val["control_type"]
            del val["left"]
            del val["top"]
            control = ft.Container(**val)

            if parent is None:
                self.keys[f"{key}"] = control
            else:
                self.keys[f"{parent}"].content.controls.append(control)

            # if "content" in val:
            #     if val["content"]["type"] == "Row":
            #         control.content = ft.Row()
            #     if val["content"]["type"] == "Column":
            #         control.content = ft.Column()

            #     for item in val["content"]["controls"]:
            #         for childKey, childVal in item.items():
            #             self.Initialize_Components(
            #                 val=childVal, key=childKey, parent=key
            #             )

            #         # Initialize_Components(self, key, val)
            #         # if val["controls"] in val["content"]:
            #         #     print("Control")
            #         # else:
            #         #     print("not kut")
            # else:
            #     return None

        # if val["control_type"] == "IconButton":
        #     control = ft.TextButton()
        #     control.width = val["width"]
        #     control.height = val["height"]
        #     control.bgcolor = val["bgcolor"]
        #     control.text = val["text"]
        #     control.icon = val["icon"]
        #     self.opacity = val.get("opacity")
        #     if self.opacity is not None:
        #         control.opacity = val["opacity"]
        #     if parent is None:
        #         self.keys[f"{key}"] = control
        #     else:
        #         control.__dict__["isChild"] = True
        #         self.keys[f"{key}"] = control
        #         self.keys[f"{parent}"].content.controls.append(control)

    def parse(self):
        widgets = self.json["widgets"]
        for key, val in widgets.items():
            # the val and the key variables are the keys and values we retrieve from the json file
            self.Initialize_Components(
                key,
                val,
            )
