import bpy


def module() -> str:
    return __name__.partition('.')[0]


def prefs() -> bpy.types.AddonPreferences:
    addons = bpy.context.preferences.addons
    return addons[module()].preferences


def save_userpref():
    preferences = bpy.context.preferences

    if preferences.use_preferences_save:
        bpy.ops.wm.save_userpref()


def popup(type: str, message: str):
    def report(self: bpy.types.Menu, context: bpy.types.Context):
        self.layout.emboss = 'NONE'
        self.layout.label(text=message)

    title = f'SIMPLE TABS {type}'
    icon = {'INFO': 'INFO', 'WARNING': 'ERROR', 'ERROR': 'CANCEL'}[type]
    bpy.context.window_manager.popup_menu(report, title, icon)
