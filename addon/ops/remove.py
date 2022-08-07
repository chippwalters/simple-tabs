import bpy
from .. import utils


class Remove(bpy.types.Operator):
    bl_idname = 'simpletabs.remove'
    bl_label = 'Remove'
    bl_description = 'Remove an item from the list'
    bl_options = {'REGISTER', 'INTERNAL'}


    def execute(self, context: bpy.types.Context):
        prefs = utils.addon.prefs()
        items = prefs.tab_items
        index = prefs.tab_index

        if index not in range(len(items)):
            return {'CANCELLED'}

        items.remove(index)
        index = min(index, len(items) - 1)

        prefs.tab_index = index
        utils.addon.save_userpref()
        return {'FINISHED'}
