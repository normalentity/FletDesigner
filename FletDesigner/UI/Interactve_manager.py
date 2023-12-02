from ..UI.Properties_Toolbar import PropertiesToolbar

class IManager():
    detail: PropertiesToolbar = None
    defualt_properties = {
        'width' : 100,
        'height' : 100,
        'opacity' : 1,
        'bg_color' : 'red',
    } # properties add them

    def __init__(self) -> None:
        pass

    # will chanage the propeties to have be if present and invisible if absent !important

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
            self.detail.control_height.content.value = defualt_properties['height']
            self.detail.control_opacity.content.value = defualt_properties['opacity']
        self.detail.control_name_space.content.value = name
        
        self.detail.update()