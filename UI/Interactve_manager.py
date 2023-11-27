from UI.Properties_Toolbar import PropertiesToolbar

class IManager():
    detail: PropertiesToolbar = None
    def __init__(self) -> None:
        pass

    def select(self, width = None, heigth=None, opacity= None, defualt_properties = None, name= None):
        if defualt_properties == None:
            # self.control_name_space,
            self.detail.control_width.content.value = width
            # self.color_box,
            self.detail.control_height.content.value = heigth
            self.detail.control_opacity.content.value = opacity
            # self.cover_component,
        else:
            self.detail.control_width.content.value = defualt_properties['width'] # could change this to use controlrefs instead
            self.detail.control_height.content.content.value = defualt_properties['height']
            self.detail.control_opacity.content.value = defualt_properties['opacity']
        self.detail.control_name_space.content.value = name
        
        self.detail.update()