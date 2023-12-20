from ..tools.create_new_file import create_new_file
import os, json, flet as ft
from ..UI.Properties_Toolbar import PropertiesToolbar
from flet import Alignment


class ParserEngine:

    """The Parser Engine is the one that responsible for saving & Editing the canvas content. It have an automatic saver built-in."""

    properties_class: PropertiesToolbar = None
    manager = None

    def __init__(self, file_path: str) -> None:
        # Project Information

        self.file_path: str = file_path

        # Checking
        self.create_the_file()

        # Experiance
        self.file_content: str = open(file_path, encoding="utf-8").read()
        self.the_content: dict = json.loads(self.file_content)
        self.__control_counter = int(
            self.the_content["page_props"]["control_counter_number"]
        )

    def create_the_file(self):
        """Check if the file is not exist, if not then create the file if not exists"""
        if not os.path.isfile(self.file_path):
            create_new_file(file_path=self.file_path)

    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))

    def load_content(self, designer_section_class):
        """Load the content into the canvas (designer)."""
        # Add the controls to the 'self.all_controls' of the designer_section_class
        if self.is_content_empty == True:
            self.edit_control_counter(value=0)
            self.control_counter = 0
        else:
            if self.control_counter > len(self.the_content["widgets"]):
                # If so, reduce the control counter to the number of widgets
                self.edit_control_counter(len(self.the_content["widgets"]))
                self.control_counter = len(self.the_content["widgets"])
        for ctrl in self.the_content["widgets"]:
            flet_cls = None
            properies = dict(self.the_content["widgets"][ctrl])
            control_type_class = properies["control_type"]
            del properies["control_type"]
            gradient = properies.get("gradient")
            if gradient == {}:
                del properies["gradient"]
                gradient = None
                # self.manager.change_property(prop="-cfg", value=False)

            if gradient is not None:
                gradient_str = properies.get("gradient")
                if gradient_str is not None:
                    begin = eval(gradient["begin"])
                    end = eval(gradient["end"])
                    color = gradient["color"]
                    properies["gradient"] = ft.LinearGradient(
                        begin=begin, end=end, colors=color
                    )
                    # self.manager.change_property(prop="-cfg", value=True)

                    # self.properties_class.change_visibility_gradient("")

            flet_cls = ft.__dict__[control_type_class](**properies)
            designer_section_class.all_controls.update({ctrl: flet_cls})
            designer_section_class.main_stack.controls.append(flet_cls)
            # Manually create a region for the control
            if flet_cls != None:
                designer_section_class.selected = flet_cls
                region1 = {
                    "begin_x": designer_section_class.selected.left,
                    "begin_y": designer_section_class.selected.top,
                    "end_x": designer_section_class.selected.left
                    + designer_section_class.selected.width,
                    "end_y": designer_section_class.selected.top
                    + designer_section_class.selected.height,
                }
                designer_section_class.all_regions.update({ctrl: region1})

            else:
                print("Please")

    # Set the control as 'selected'

    def save_all(self):
        """This function will save all the changes by overwrite the content in the file."""
        open(self.file_path, "w+", encoding="utf-8").write(
            json.dumps(self.the_content, indent=4)
        )

    def add_new_control_to_content(
        self, control_uniqe_name: str, control_dict: dict, control_class_name: str
    ):
        """Add new control to content."""
        self.the_content["widgets"].update({control_uniqe_name: control_dict})
        self.the_content["widgets"][control_uniqe_name][
            "control_type"
        ] = control_class_name
        self.save_all()

    # def parse_gradient(self, gradient_str):
    #     # Remove the 'ft.LinearGradient' from the start and the parentheses from the ends
    #     gradient_str = gradient_str.replace("ft.LinearGradient(", "")[:-1]

    #     # Split the string into components
    #     components = gradient_str.split(",")

    #     # Parse each component
    #     begin = eval(components[0].split("=")[1])
    #     end = eval(components[1].split("=")[1])

    #     # The color component is a list, so it might be split into multiple components
    #     # Join all components from the third one onwards into a single string, and evaluate it to get the color list
    #     color_str = ",".join(components[2:]).split("=")[1]
    #     # color_str = color_str.replace("#", "'#").replace(",", "',")[:-1] + "']"
    #     color = eval(color_str.strip())

    #     # Return the ft.LinearGradient object
    #     return ft.LinearGradient(begin=begin, end=end, colors=color)

    def edit_control_property(
        self, control_uniqe_name: str, property_name: str, new_property_value=None
    ):
        """Edit an existed control's property. It need the control order number in the `widgets` list."""
        if control_uniqe_name not in self.the_content["widgets"]:
            raise Exception(
                f"There is no existing control with name '{control_uniqe_name}'"
            )
        if property_name != "gradient":
            self.the_content["widgets"][control_uniqe_name][
                property_name
            ] = new_property_value
        if property_name == "gradient":
            self.the_content["widgets"][control_uniqe_name][
                property_name
            ] = new_property_value

        self.save_all()

    def delete_control_property(self, control_uniqe_name: str):
        """Delete an existed control. It need the control order number in the `widgets` list."""
        del self.the_content["widgets"][control_uniqe_name]
        self.save_all()

    def get_new_control_counter_number(self) -> int:
        self.control_counter = self.control_counter + 1
        return self.control_counter

    def edit_control_counter(self, value):
        self.the_content["page_props"].update({"control_counter_number": value})
        # self.control_counter = value

        self.save_all()

    # Properties
    @property
    def is_content_empty(self):
        """Returns `True` if there is not widgets in the page, Meaning that there is no content."""
        if self.the_content["widgets"] == {}:
            return True
        return False

    @property
    def control_counter(self):
        """Returns the current control counter number"""
        return self.__control_counter

    @control_counter.setter
    def control_counter(self, new_value: int):
        if not isinstance(new_value, int):
            raise ValueError(
                f"control_counter accept value with type 'int' only, not {type(new_value)}"
            )

        self.the_content["page_props"]["control_counter_number"] = (
            self.the_content["page_props"]["control_counter_number"] + 1
        )

        self.__control_counter = new_value
        self.save_all()
