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

        # TODO: Set the sidebar width (if possible)

        for panel in utils.sidebar.panels():
            if hasattr(panel, 'original_category'):
                panel.bl_category = panel.original_category
                del panel.original_category
                utils.sidebar.update(panel)

            elif utils.sidebar.category(panel) == self.category:
                panel.original_category = getattr(panel, 'bl_category', None)
                panel.bl_category = 'SIMPLE TABS'
                utils.sidebar.update(panel)

        self.report({'INFO'}, f'Opened {self.category}')
        return {'FINISHED'}
