from .Properties_Toolbar import (
    ContainerPropertiesToolbar,
    ElevatedButtonPropertiesToolbar,
)

from ..Parser.parser import ParserEngine
import flet as ft


# ft.ElevatedButton().b


class IManager:
    object_controller = None
    # detail
    eb: ContainerPropertiesToolbar = None
    defualt_properties = {
        "width": "",
        "height": "",
        "opacity": "",
        "bg_color": "",
    }  # properties add them
    page = None

    def __init__(self, parser_engine: ParserEngine) -> None:
        self.parser_engine = parser_engine
        self.detail: ContainerPropertiesToolbar = ContainerPropertiesToolbar(
            manager=self, parser_engine=self.parser_engine, page=self.page
        )

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
        # nmn=None,
    ):
        self.defualt_properties11 = defualt_properties

        # if defualt_properties == None:
        if self.object_controller.selected is None:
            self.detail.propertiesContainer.visible = False
            self.detail.control_width.content.value = width
            self.detail.control_height.content.value = heigth
            self.detail.control_opacity.content.value = opacity
            # self.color_box,
        else:
            old_detail = self.detail
            if isinstance(self.object_controller.selected, ft.ElevatedButton):
                self.detail = ElevatedButtonPropertiesToolbar(
                    manager=self, parser_engine=self.parser_engine, page=self.page
                )

                # self.object_controller.selected.disabled = False
                self.eb.update_displayarea()
                self.page.update()
            if isinstance(self.object_controller.selected, ft.Container):
                self.detail = ContainerPropertiesToolbar(
                    manager=self, parser_engine=self.parser_engine, page=self.page
                )
                # self.detail.update()

                self.eb.update_displayarea()
                self.page.update()

            self.detail.update()
            self.page.update()
            # self.eb.propertiesContainer.visible = True
            # if nmn=="El"
            self.detail.propertiesContainer.visible = True
            self.detail.control_width.content.value = defualt_properties[
                "width"
            ]  # could change this to use controlrefs instea
            self.detail.control_height.content.value = defualt_properties["height"]
            # self.detail.control_border_radius.content.value = defualt_properties[
            #     "borderradius"
            # ]
            check = defualt_properties.get("gradient")
            if check is not None:
                self.detail.gradient_switch.content.value = True
                self.detail.cover_component.visible = True
                # if check is None:
                #     print(check)

                if (
                    self.parser_engine.the_content["widgets"][
                        self.object_controller.unique_name
                    ]["gradient"]
                    == {}
                ):
                    self.detail.gradient_switch.content.value = False
                    self.detail.cover_component.visible = False
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
        if prop == "-o":
            if self.object_controller.selected is not None:
                if value.replace(".", "").isnumeric() and value.__contains__("."):
                    self.object_controller.selected.opacity = float(value)
                    self.parser_engine.edit_control_property(
                        control_uniqe_name=self.object_controller.unique_name,
                        property_name="opacity",
                        new_property_value=float(value),
                    )
                    self.object_controller.selected.update()
                    self.object_controller.show_outline()
        if prop == "-w":
            if self.object_controller.selected is not None:
                if value := self.check_value("x", value):
                    self.object_controller.selected.width = value

                    self.parser_engine.edit_control_property(
                        control_uniqe_name=self.object_controller.unique_name,
                        property_name="width",
                        new_property_value=value,
                    )
                    self.object_controller.selected.update()
                    self.object_controller.show_outline()
        if prop == "-del":
            if self.object_controller.selected is not None:
                self.parser_engine.delete_control_property(
                    control_uniqe_name=self.object_controller.unique_name
                )

                if (
                    self.object_controller.selected
                    in self.object_controller.main_stack.controls
                ):
                    self.object_controller.main_stack.controls.remove(
                        self.object_controller.selected
                    )

                if (
                    self.object_controller.outlineContainer
                    in self.object_controller.main_stack.controls
                ):
                    self.object_controller.outlineContainer.visible = False

                self.object_controller.main_stack.update()

                selected_name = self.object_controller.unique_name

                # remove the selected item from all_controls
                if selected_name in self.object_controller.all_controls:
                    del self.object_controller.all_controls[selected_name]

                # remove the selected item from all_regions
                if selected_name in self.object_controller.all_regions:
                    del self.object_controller.all_regions[selected_name]

                # self.parser_engine.load_content(
                #     designer_section_class=self.object_controller
                # )
                self.parser_engine.the_content["page_props"][
                    "control_counter_number"
                ] = (
                    self.parser_engine.the_content["page_props"][
                        "control_counter_number"
                    ]
                    - 1
                )
                self.parser_engine.control_counter = (
                    self.parser_engine.control_counter - 1
                )

                self.detail.propertiesContainer.visible = False
                self.detail.propertiesContainer.update()
                

        if prop == "-h":
            if self.object_controller.selected is not None:
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
            if self.object_controller.selected is not None:
                self.object_controller.selected.bgcolor = value  # check if this exists
                if isinstance(self.object_controller.selected, ft.ElevatedButton):
                    self.object_controller.selected.disabled = False
                self.parser_engine.edit_control_property(
                    control_uniqe_name=self.object_controller.unique_name,
                    property_name="bgcolor",
                    new_property_value=value,
                )

                self.object_controller.selected.update()
                self.object_controller.show_outline()
                if isinstance(self.object_controller.selected, ft.ElevatedButton):
                    self.object_controller.selected.disabled = True
                self.detail.hex_holder.content.value = value
                self.object_controller.selected.update()
                self.object_controller.show_outline()
        if prop == "-b":
            if self.object_controller.selected is not None:
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
            if self.object_controller.selected is not None:
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

                self.grad = (
                    self.object_controller.selected.gradient
                ) = ft.LinearGradient(
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
                self.detail.gradient_hex_holder.update()
                self.detail.gradient_hex_holder1.update()
                self.object_controller.selected.update()
                self.object_controller.show_outline()
        if prop == "-gcr":
            if self.object_controller.selected is not None:
                # if self.object_controller.selected.gradient is None:
                self.object_controller.selected.gradient = None
                self.parser_engine.edit_control_property(
                    control_uniqe_name=self.object_controller.unique_name,
                    property_name="gradient",
                    new_property_value={},
                )
                self.defualt_properties11["gradient"] = ""
                # print(f'from gcr{self.defualt_properties11["gradient"]}')
                # print(f"from gcr{self.defualt_properties11}")
                self.object_controller.selected.update()
                self.object_controller.show_outline()
        if prop == "-change_begin":
            if self.object_controller.selected is not None:
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
            if self.object_controller.selected is not None:
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
            if self.object_controller.selected is not None:
                self.object_controller.selected.gradient.rotation = rotation
                self.object_controller.selected.update()
        if prop == "-t":
            if self.object_controller.selected is not None:
                self.object_controller.selected.text = value
                self.object_controller.selected.update()
                self.parser_engine.edit_control_property(
                    control_uniqe_name=self.object_controller.unique_name,
                    property_name="text",
                    new_property_value=value,
                )
        if prop == "-ctrlname":
            if (
                str(self.object_controller.unique_name)
                in self.parser_engine.the_content["widgets"]
            ):
                # Check if the new key already exists in the widgets dictionary
                if value in self.parser_engine.the_content["widgets"]:
                    print(f"Key {value} already exists in widgets dictionary.")
                else:
                    self.parser_engine.the_content["widgets"][
                        value
                    ] = self.parser_engine.the_content["widgets"].pop(
                        str(self.object_controller.unique_name)
                    )
                    # Update the unique_name attribute of the object_controller
                    self.object_controller.unique_name = value
            else:
                print(
                    f"Key {str(self.object_controller.unique_name)} not found in widgets dictionary."
                )
            self.parser_engine.save_all()

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
