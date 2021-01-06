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

        row = column.row()
        rows = max(len(prefs.tab_items), 8)
        row.template_list("SIMPLETABS_UL_TabList", '', prefs, 'tab_items', prefs, 'tab_index', rows=rows)

        col = row.column(align=True)
        col.scale_x = 1.25
        col.scale_y = 1.5

        col.operator('wm.save_userpref', text='', icon='PREFERENCES')
        col.separator()
        col.operator('simpletabs.refresh', text='', icon='FILE_REFRESH')
        col.operator('simpletabs.update', text='', icon='CHECKMARK')
        col.separator()
        col.operator('simpletabs.move', text='', icon='TRIA_UP').direction = 'UP'
        col.operator('simpletabs.move', text='', icon='TRIA_DOWN').direction = 'DOWN'
        col.separator()
        col.operator('wm.url_open', text='', icon_value=icons.id('question')).url = 'http://cw1.me/simpletabd'


def popover(self, context: bpy.types.Context):
    layout = self.layout
    panel = MainPanel.bl_idname
    icon = icons.id('simple-tabs')
    layout.popover(panel, text='', icon_value=icon)
