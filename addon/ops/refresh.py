import bpy
from .. import utils


class Refresh(bpy.types.Operator):
    bl_idname = 'simpletabs.refresh'
    bl_label = 'Refresh'
    bl_description = 'Refresh the list, so it is synchronized with the sidebar'
    bl_options = {'REGISTER', 'INTERNAL'}


    def execute(self, context: bpy.types.Context):
        if hasattr(context.space_data, 'show_region_ui'):
            if not context.space_data.show_region_ui:
                context.space_data.show_region_ui = True

        prefs = utils.addon.prefs()
        names = utils.sidebar.tabs()

        if utils.hops.get_module():
            names.add(utils.hops.get_default())

        if utils.bc.get_module():
            names.add(utils.bc.get_default())

        for tab in prefs.tab_items[:]:
            if tab.name not in names:
                index = prefs.tab_items.find(tab.name)
                prefs.tab_items.remove(index)

        for name in names:
            if name not in prefs.tab_items:
                tab = prefs.tab_items.add()
                tab.name = name

                if name == utils.hops.get_default():
                    tab.rename = utils.hops.get_tab()

                elif name == utils.bc.get_default():
                    tab.rename = utils.bc.get_tab()

                else:
                    tab.rename = name

        self.report({'INFO'}, f'Found {len(prefs.tab_items)} tabs')
        return {'FINISHED'}
