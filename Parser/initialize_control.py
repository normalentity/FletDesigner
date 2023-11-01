import flet as ft


def Initialize_Components(self, key, val):
    if val["type"] == "Container":
        self.keys[f"{key}"] = ft.Container()
        self.keys[f"{key}"].width = val["width"]
        self.keys[f"{key}"].height = val["height"]
        self.keys[f"{key}"].opacity = val["opacity"]
        self.keys[f"{key}"].bgcolor = val["bgcolor"]
        self.keys[f"{key}"].border_radius = ft.border_radius.all(val["border_radius"])
        self.padding = val.get("padding")
        if self.padding is not None:
            left = val["padding"]["left"]
            right = val["padding"]["right"]
            bottom = val["padding"]["bottom"]
            top = val["padding"]["top"]
            self.keys[f"{key}"].padding = ft.padding.only(
                left=left, right=right, bottom=bottom, top=top
            )

        if "content" in val:
            if val["content"]["type"] == "Row":
                self.keys[f"c1"].content = ft.Row()

                # if isinstance(val["content"]["controls"], list):
                for item in val["content"]["controls"]:
                    for key, val in item.items():
                        self.Initialize_Components(val=val, key=key)
                    # Initialize_Components(self, key, val)
        else:
            return None

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



