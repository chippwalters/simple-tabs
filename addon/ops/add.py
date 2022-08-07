import bpy
from .. import utils


class Add(bpy.types.Operator):
    bl_idname = 'simpletabs.add'
    bl_label = 'Add'
    bl_description = 'Add an item to the list'
    bl_options = {'REGISTER', 'INTERNAL'}


    name: bpy.props.StringProperty(name='Tab Name')


    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        self.name = ''
        return context.window_manager.invoke_props_dialog(self)


    def execute(self, context: bpy.types.Context):
        prefs = utils.addon.prefs()
        items = prefs.tab_items

        if not self.name:
            self.report({'ERROR'}, 'You have to set a name')
            return {'CANCELLED'}

        if self.name in items:
            self.report({'ERROR'}, 'Tab name already exists')
            return {'CANCELLED'}

        tab = items.add()
        tab.name = self.name
        tab.rename = self.name

        prefs.tab_index = len(items) - 1
        utils.addon.save_userpref()
        return {'FINISHED'}
