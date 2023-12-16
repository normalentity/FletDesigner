from .Properties_Toolbar import PropertiesToolbar
from ..Parser.parser import ParserEngine
import flet as ft


class IManager:
    detail: PropertiesToolbar = None
    object_controller = None
    defualt_properties = {
        "width": "",
        "height": "",
        "opacity": "",
        "bg_color": "",
    }  # properties add them

    def __init__(self, parser_engine: ParserEngine) -> None:
        self.parser_engine = parser_engine

    # def submit(self, e):
    #     self.defualt_properties.u

    # will chanage the propeties to have be if present and invisible if absent !important

    def select(
        self,
        width=None,
        heigth=None,
        opacity=None,
        defualt_properties=None,
        name=None,
        unique_name=None,
    ):
        if defualt_properties == None:
            self.detail.control_width.content.value = width
            self.detail.control_height.content.value = heigth
            self.detail.control_opacity.content.value = float(opacity)
            # self.color_box,
        else:
            self.detail.control_width.content.value = defualt_properties[
                "width"
            ]  # could change this to use controlrefs instea
            self.detail.control_height.content.value = defualt_properties["height"]
            self.detail.control_border_radius.content.value = defualt_properties[
                "borderradius"
            ]
            check = defualt_properties.get("gradient")
            if check is not None:
                print(f"from f1{defualt_properties['gradient']}")
                if defualt_properties["gradient"] != {}:
                    gradient = defualt_properties["gradient"]
            if check is not None:
                print(f"from f2{defualt_properties['gradient']}")
                if defualt_properties["gradient"] == {}:
                    self.detail.gradient_switch.content.value = False
                    self.detail.cover_component.visible = False

            if check is not None:
                print(f"from f3{defualt_properties['gradient']}")
                if defualt_properties["gradient"] != {}:
                    self.detail.gradient_switch.content.value = True
                    self.detail.cover_component.visible = True

            if defualt_properties["opacity"] != "":
                defualt_properties["opacity"] = float(
                    defualt_properties["opacity"]
                )  # change incase
            self.detail.control_opacity.content.value = defualt_properties["opacity"]
        self.detail.control_name_space.content.value = name
        self.detail.update()

    def change_property(
        self,
        prop: str,
        value=None,
        end=None,
        value_gradient=None,
        begin=None,
        rotation=None,
    ):
        if self.object_controller.selected is not None:
            control_unique_name = self.object_controller.control_to_name.get(
                self.object_controller.selected
            )

            # print(self.object_controller.selected.__dict__.get("Unique_Name"))
            # print(self.object_controller.selected)

            # print(self.object_controller.unique_name)

            # print(self.object_controller.selected.__dict__)

        if prop == "-o":
            if value.replace(".", "").isnumeric() and value.__contains__("."):
                self.object_controller.selected.opacity = float(value)
                self.parser_engine.edit_control_property(
                    control_uniqe_name=self.object_controller.unique_name,
                    property_name="opacity",
                    new_property_value=float(value),
                )
                self.object_controller.selected.update()
            self.object_controller.show_outline()
            # self.detail.gradient_switch.content.value = value
            # self.detail.change_visibilty_gradient(e="")
            print(self.detail.cover_component)
        if prop == "-w":
            if value := self.check_value("x", value):
                self.object_controller.selected.width = value

                self.parser_engine.edit_control_property(
                    control_uniqe_name=self.object_controller.unique_name,
                    property_name="width",
                    new_property_value=value,
                )
                self.object_controller.selected.update()
                self.object_controller.show_outline()
        if prop == "-h":
            if value := self.check_value("y", value):
                self.object_controller.selected.height = value
                self.parser_engine.edit_control_property(
                    control_uniqe_name=self.object_controller.unique_name,
                    property_name="height",
                    new_property_value=value,
                )
                self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-c":
            self.object_controller.selected.bgcolor = value  # check if this exists
            self.parser_engine.edit_control_property(
                control_uniqe_name=self.object_controller.unique_name,
                property_name="bgcolor",
                new_property_value=value,
            )

            self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-b":
            self.object_controller.selected.border_radius = int(value)
            # self.object_controller.outlineContainer.border_radius = int(value)
            self.parser_engine.edit_control_property(
                control_uniqe_name=self.object_controller.unique_name,
                property_name="border_radius",
                new_property_value=int(value),
            )
            self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-gc":
            # if self.object_controller.selected.gradient is None:
            if value:
                self.color1 = value
                self.last_color1 = (
                    value  # Store the last color value chosen by the user
                )
            else:
                self.color1 = (
                    self.last_color1
                    if hasattr(self, "last_color1")
                    else ft.colors.CYAN_100
                )

            if value_gradient:
                self.color2 = value_gradient
                self.last_color2 = (
                    value_gradient  # Store the last color value chosen by the user
                )
            else:
                self.color2 = (
                    self.last_color2
                    if hasattr(self, "last_color2")
                    else ft.colors.DEEP_PURPLE_ACCENT
                )

            self.grad = self.object_controller.selected.gradient = ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
                colors=[self.color1, self.color2],
            )

            self.new_gradient_prop_value = {
                "begin": "ft.alignment.top_right",
                "end": "ft.alignment.bottom_left",
                "color": [f"{self.color1}", f"{self.color2}"],
            }
            self.parser_engine.edit_control_property(
                control_uniqe_name=self.object_controller.unique_name,
                property_name="gradient",
                new_property_value=self.new_gradient_prop_value,
            )

            self.object_controller.selected.update()
            self.detail.gradient_hex_holder.content.value = self.color1
            self.detail.gradient_hex_holder1.content.value = self.color2
            self.detail.gradient_color_holder.bgcolor = self.color1
            self.detail.gradient_color_holder1.bgcolor = self.color2
            self.detail.gradient_hex_holder.update()
            self.detail.gradient_hex_holder1.update()
            self.detail.gradient_color_holder.update()
            self.detail.gradient_color_holder1.update()
            self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-gcr":
            # if self.object_controller.selected.gradient is None:
            self.object_controller.selected.gradient = None
            self.parser_engine.edit_control_property(
                control_uniqe_name=self.object_controller.unique_name,
                property_name="gradient",
                new_property_value={},
            )
            self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-change_begin":
            end_value = ft.alignment.top_left  # Default value
            if self.detail.choose_end.content.value == "top_left":
                end_value = ft.alignment.top_left
            self.object_controller.selected.gradient.end = end_value
            self.new_gradient_prop_value.update({"end": f"{end_value}"})
            self.object_controller.selected.gradient.begin = begin
            self.new_gradient_prop_value.update({"begin": f"{begin}"})
            self.parser_engine.edit_control_property(
                control_uniqe_name=self.object_controller.unique_name,
                property_name="gradient",
                new_property_value=self.new_gradient_prop_value,
            )
            self.object_controller.selected.update()
            self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-change_end":
            self.object_controller.selected.gradient.end = end
            self.new_gradient_prop_value.update({"end": f"{end}"})
            self.parser_engine.edit_control_property(
                control_uniqe_name=self.object_controller.unique_name,
                property_name="gradient",
                new_property_value=self.new_gradient_prop_value,
            )
            self.object_controller.selected.update()
            self.object_controller.selected.update()
            self.object_controller.show_outline()
        if prop == "-rotation":
            self.object_controller.selected.gradient.rotation = rotation
            self.object_controller.selected.update()

    def check_value(self, region="x", value="0"):
        if value.isnumeric():
            value = int(value)
            if value != 0:
                item = self.object_controller.all_regions[
                    self.object_controller.itemName
                ]
                item["end_" + region] += (
                    -(item["end_" + region] - item["begin_" + region]) + value
                )
                return value
        return False
