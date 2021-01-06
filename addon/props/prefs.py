import bpy
from .. import props
from .. import utils


def update_exclude_tabs(self, context):
    exclude = [tab.strip() for tab in self.exclude_tabs.split(',')]

    if 'Item' not in exclude:
        exclude.insert(0, 'Item')

    self['exclude_tabs'] = ', '.join(tab for tab in exclude if tab)


class AddonPrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon.module()


    popover_width: bpy.props.FloatProperty(
        name='Popover Width',
        description='Width of the 3D view popover in UI units',
        default=16,
        min=8,
        max=32,
        step=1,
        precision=2,
    )


    startup_delay: bpy.props.FloatProperty(
        name='Startup Delay',
        description='How many seconds to wait after blender startup before panels',
        default=5,
        min=1,
        max=20,
        step=1,
        precision=2,
    )


    exclude_tabs: bpy.props.StringProperty(
        name='Exclude Tabs',
        description='A comma separated list of tabs that SIMPLE TABS should ignore',
        default='Item, ',
        update=update_exclude_tabs,
    )


    tab_items: bpy.props.CollectionProperty(type=props.tab.TabProps)
    tab_index: bpy.props.IntProperty(name='', description='Ignore the sentence above')


    def draw(self, context: bpy.types.Context):
        layout = self.layout
        column = layout.column()

        split = column.split(factor=0.5)
        split.label(text='Popover Width')
        split.prop(self, 'popover_width', text='')

        split = column.split(factor=0.5)
        split.label(text='Startup Delay')
        split.prop(self, 'startup_delay', text='')

        split = column.split(factor=0.5)
        split.label(text='Exclude Tabs')
        split.prop(self, 'exclude_tabs', text='')
