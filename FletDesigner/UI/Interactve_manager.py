from ..UI.Properties_Toolbar import PropertiesToolbar

class IManager():
    detail: PropertiesToolbar = None
    object_controller = None
    defualt_properties = {
        'width' : "",
        'height' : "",
        'opacity' : "",
        'bg_color' : "",
    } # properties add them

    def __init__(self) -> None:
        pass

    # will chanage the propeties to have be if present and invisible if absent !important

    def select(self, width = None, heigth=None, opacity= None, defualt_properties = None, name= None):
        if defualt_properties == None:
            self.detail.control_width.content.value = width
            self.detail.control_height.content.value = heigth
            self.detail.control_opacity.content.value = float(opacity)
            # self.color_box,
        else:
            self.detail.control_width.content.value = defualt_properties['width'] # could change this to use controlrefs instead
            self.detail.control_height.content.value = defualt_properties['height']
            if defualt_properties['opacity'] != '': defualt_properties['opacity'] = float(defualt_properties['opacity']) # change incase
            self.detail.control_opacity.content.value = defualt_properties['opacity']
        self.detail.control_name_space.content.value = name
        self.detail.update()
    
    def change_property(self, prop:str, value:str):
        self.object_controller.outlineContainer.visible = False
        self.object_controller.outlineContainer.update()
        if prop == '-o':
            if value.replace('.', '').isnumeric() and value.__contains__('.'):
                self.object_controller.selected.opacity = float(value)
        if prop == '-w':
            if value := self.check_value('x', value):
                self.object_controller.selected.width = value
        if prop == '-h':
            if value := self.check_value('y', value):
                self.object_controller.selected.height = value
        if prop == '-c':
            self.object_controller.selected.bgcolor = value # check if this exists
            
        self.object_controller.selected.update()
        self.object_controller.show_outline()
    
    def check_value(self, region= 'x', value = '0'):
        if value.isnumeric():
            value = int(value)
            if value != 0:
                item = self.object_controller.all_regions[self.object_controller.itemName]
                item['end_'+region] += -(item['end_'+region] - item['begin_'+region]) + value
                return value
        return False