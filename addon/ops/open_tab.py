import bpy
from .. import utils


class OpenTab(bpy.types.Operator):
    bl_idname = 'simpletabs.open_tab'
    bl_label = 'Open Tab'
    bl_description = 'Open the chosen tab in the sidebar'
    bl_options = {'REGISTER', 'INTERNAL'}


    category: bpy.props.StringProperty(
        name='Category',
        description='Which sidebar category to open',
        default='',
    )


    def execute(self, context: bpy.types.Context):
        if not context.space_data.show_region_ui:
            context.space_data.show_region_ui = True

        panels = utils.sidebar.panels()

        for panel in panels:
            if utils.sidebar.category(panel) == self.category:
                utils.sidebar.update(panel)

        for panel in panels:
            if utils.sidebar.category(panel) != self.category:
                utils.sidebar.update(panel)

        self.report({'INFO'}, f'Opened {self.category}')
        return {'FINISHED'}
