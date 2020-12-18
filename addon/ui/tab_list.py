import bpy


class TabList(bpy.types.UIList):
    bl_idname = 'SIMPLETABS_UL_TabList'


    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name)
        layout.prop(item, 'rename', text='')
