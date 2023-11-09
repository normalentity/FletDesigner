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
        if val["type"] == "Container":
            # self.keys[f"{key}"] = ft.Container()
            control = ft.Container()
            control.width = val["width"]
            control.height = val["height"]
            control.opacity = val["opacity"]
            control.bgcolor = val["bgcolor"]
            control.border_radius = ft.border_radius.all(val["border_radius"])
            self.padding = val.get("padding")
            if self.padding is not None:
                left = val["padding"]["left"]
                right = val["padding"]["right"]
                bottom = val["padding"]["bottom"]
                top = val["padding"]["top"]
                control.padding = ft.padding.only(
                    left=left, right=right, bottom=bottom, top=top
                )

            if parent is None:
                self.keys[f"{key}"] = control
            else:
                self.keys[f"{parent}"].content.controls.append(control)

            if "content" in val:
                if val["content"]["type"] == "Row":
                    control.content = ft.Row()
                    print(control.content)
                if val["content"]["type"] == "Column":
                    control.content = ft.Column()
                    print(control.content)

                    # if isinstance(val["content"]["controls"], list):
                    for item in val["content"]["controls"]:
                        for childKey, childVal in item.items():
                            self.Initialize_Components(
                                val=childVal, key=childKey, parent=key
                            )

                        # Initialize_Components(self, key, val)
                        # if val["controls"] in val["content"]:
                        #     print("Control")
                        # else:
                        #     print("not kut")
            else:
                return None

        if val["type"] == "IconButton":
            control = ft.TextButton()
            control.width = val["width"]
            control.height = val["height"]
            control.bgcolor = val["bgcolor"]
            control.text = val["text"]
            control.icon = val["icon"]
            self.opacity = val.get("opacity")
            if self.opacity is not None:
                control.opacity = val["opacity"]
            if parent is None:
                self.keys[f"{key}"] = control
            else:
                control.__dict__["isChild"] = True
                self.keys[f"{key}"] = control
                self.keys[f"{parent}"].content.controls.append(control)

    def parse(self):
        for item in self.json:
            for key, val in item.items():
                # the val and the key variables are the keys and values we retrieve from the json file
                self.Initialize_Components(
                    key,
                    val,
                )

    def Add_Widgets(self, Control):
        pass
