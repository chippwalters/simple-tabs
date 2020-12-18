import bpy
from .. import props
from .. import utils


class AddonPrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon.module()


    popover_width: bpy.props.FloatProperty(
        name='Popover Width',
        description='Width of the 3D view popover in UI units',
        default=8,
        min=4,
        max=16,
        step=1,
        precision=2,
    )


    tab_items: bpy.props.CollectionProperty(type=props.tab.TabProps)
    tab_index: bpy.props.IntProperty(name='', description='Ignore the sentence above')


    def draw(self, context: bpy.types.Context):
        layout = self.layout
        column = layout.column()

        split = column.split(factor=0.5)
        split.label(text='Popover Width')
        split.prop(self, 'popover_width', text='')
