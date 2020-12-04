import bpy


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

        # TODO: Set the sidebar width
        # TODO: Actually open the tab

        self.report({'INFO'}, f'Opened {self.category}')
        return {'FINISHED'}
