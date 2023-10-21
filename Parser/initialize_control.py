import flet as ft


def Initialize_Components(self, key, val):
    if val["type"] == "Container":
        self.keys[f"{key}"] = ft.Container()
        self.keys[f"{key}"].width = val["width"]
        self.keys[f"{key}"].height = val["height"]
        self.keys[f"{key}"].opacity = val["opacity"]
        self.keys[f"{key}"].bgcolor = val["bgcolor"]
        self.keys[f"{key}"].border_radius = ft.border_radius.all(val["border_radius"])
        self.keys[f"{key}"].content = ft.Row()
        self.padding = val.get("padding")
        if self.padding is not None:
            self.keys[f"{key}"].padding = ft.padding.only(left=val["padding"])
    if val["type"] == "IconButton":
        self.keys[f"{key}"] = ft.TextButton()
        self.keys[f"{key}"].width = val["width"]
        self.keys[f"{key}"].height = val["height"]
        self.keys[f"{key}"].bgcolor = val["bgcolor"]
        self.keys[f"{key}"].text = val["text"]
        self.keys[f"{key}"].icon = val["icon"]
        self.opacity = val.get("opacity")
        if self.opacity is not None:
            self.keys[f"{key}"].opacity = val["opacity"]

        self.keys[f"c1"].content.controls.append(self.keys[f"{key}"])
