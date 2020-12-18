import bpy
from .. import utils


class Move(bpy.types.Operator):
    bl_idname = 'simpletabs.move'
    bl_label = 'Move'
    bl_description = 'Move an item in the list'
    bl_options = {'REGISTER', 'INTERNAL'}


    direction: bpy.props.EnumProperty(
        items=[
            ('UP', 'Up', 'Move the item up'),
            ('DOWN', 'Down', 'Move the item down'),
        ],
        options={'HIDDEN'},
    )


    def execute(self, context: bpy.types.Context):
        prefs = utils.addon.prefs()
        items = prefs.tab_items
        index = prefs.tab_index

        direction = 1 if self.direction == 'DOWN' else -1
        neighbor = max(0, index + direction)
        items.move(neighbor, index)
        length = max(0, len(items) - 1)
        index = max(0, min(neighbor, length))

        prefs.tab_index = index
        return {'FINISHED'}
