import bpy
from .. import utils
from .. import icons


class MainPanel(bpy.types.Panel):
    bl_idname = 'SIMPLETABS_PT_MainPanel'
    bl_label = 'SIMPLE TABS'
    bl_category = ''
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'


    def draw(self, context: bpy.types.Context):
        prefs = utils.addon.prefs()

        layout = self.layout
        column = layout.column()

        if self.is_popover:
            layout.ui_units_x = prefs.popover_width

        for category in sorted(utils.sidebar.categories()):
            op = column.operator('simpletabs.open_tab', text=category)
            op.category = category


def popover(self, context: bpy.types.Context):
    layout = self.layout
    panel = MainPanel.bl_idname
    icon = icons.id('simple-tabs')
    layout.popover(panel, text='', icon_value=icon)
