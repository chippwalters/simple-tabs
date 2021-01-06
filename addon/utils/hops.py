import bpy


def get_default() -> str:
    return 'HardOps'


def get_module() -> str:
    wm = bpy.context.window_manager
    return getattr(wm, 'Hard_Ops_folder_name', None)


def get_prefs() -> bpy.types.AddonPreferences:
    module = get_module()

    if module is not None:
        addons = bpy.context.preferences.addons
        return addons[module].preferences


def get_tab() -> str:
    prefs = get_prefs()

    if prefs is not None:
        return prefs.ui.Hops_panel_location


def set_tab(tab: str):
    prefs = get_prefs()

    if prefs is not None:
        prefs.ui.Hops_panel_location = tab
