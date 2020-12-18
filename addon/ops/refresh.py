import bpy
from .. import utils


class Refresh(bpy.types.Operator):
    bl_idname = 'simpletabs.refresh'
    bl_label = 'Refresh'
    bl_description = 'Refresh the list, so it is synchronized with the sidebar'
    bl_options = {'REGISTER', 'INTERNAL'}


    def execute(self, context: bpy.types.Context):
        prefs = utils.addon.prefs()
        names = utils.sidebar.tabs()

        for tab in prefs.tab_items[:]:
            if tab.name not in names:
                index = prefs.tab_items.find(tab.name)
                prefs.tab_items.remove(index)

        for name in names:
            if name not in prefs.tab_items:
                tab = prefs.tab_items.add()
                tab.name = name
                tab.rename = name

        self.report({'INFO'}, f'Found {len(prefs.tab_items)} tabs')
        return {'FINISHED'}
