import bpy
from .. import utils


class Update(bpy.types.Operator):
    bl_idname = 'simpletabs.update'
    bl_label = 'Update'
    bl_description = 'Update the sidebar to synchronize with your settings here'
    bl_options = {'REGISTER', 'INTERNAL'}


    def execute(self, context: bpy.types.Context):
        if hasattr(context.space_data, 'show_region_ui'):
            if not context.space_data.show_region_ui:
                context.space_data.show_region_ui = True

        prefs = utils.addon.prefs()
        panels = utils.sidebar.panels()

        for panel in panels[:]:
            if utils.sidebar.tab(panel) not in prefs.tab_items:
                panels.remove(panel)

        for panel in panels:
            if getattr(panel, 'original_category', None):
                panel.bl_category = panel.original_category
                del panel.original_category

        for panel in panels:
            panel.original_category = utils.sidebar.tab(panel)
            tab = prefs.tab_items[panel.original_category]
            panel.bl_category = tab.rename

        panels_per_tab = {tab.name: [] for tab in prefs.tab_items}

        for panel in panels:
            tab = utils.sidebar.tab(panel)
            panels_per_tab[tab].append(panel)

        for tab in prefs.tab_items:
            if tab.name == utils.hops.get_default():
                utils.hops.set_tab(tab.rename)

            elif tab.name == utils.bc.get_default():
                utils.bc.set_tab(tab.rename)

            else:
                for panel in panels_per_tab[tab.name]:
                    utils.sidebar.update(panel)

        self.report({'INFO'}, 'Updated sidebar tabs')
        return {'FINISHED'}
