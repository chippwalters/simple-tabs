import bpy
from . import tab
from . import prefs
from . import addon


classes = (
    tab.TabProps,
    prefs.AddonPrefs,
    addon.AddonProps,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.simpletabs = bpy.props.PointerProperty(type=addon.AddonProps)


def unregister():
    del bpy.types.WindowManager.simpletabs

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
