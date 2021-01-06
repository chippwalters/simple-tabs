import bpy


def get_default() -> str:
    return 'BoxCutter'


def get_module() -> str:
    wm = bpy.context.window_manager
    props = getattr(wm, 'bc', None)
    return getattr(props, 'addon', None)


def get_prefs() -> bpy.types.AddonPreferences:
    module = get_module()

    if module is not None:
        addons = bpy.context.preferences.addons
        return addons[module].preferences


def get_tab() -> str:
    prefs = get_prefs()

    if prefs is not None:
        return prefs.display.tab


def set_tab(tab: str):
    prefs = get_prefs()

    if prefs is not None:
        prefs.display.tab = tab
