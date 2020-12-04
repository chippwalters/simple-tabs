import bpy


def module() -> str:
    return __name__.partition('.')[0]


def prefs() -> bpy.types.AddonPreferences:
    addons = bpy.context.preferences.addons
    return addons[module()].preferences
