import bpy
import inspect
import traceback
from .. import utils


def tab(panel: bpy.types.Panel) -> str:
    if getattr(panel, 'bl_parent_id', None):
        parent = getattr(bpy.types, panel.bl_parent_id, None)

        if parent:
            return tab(parent)

    if getattr(panel, 'original_category', None):
        return panel.original_category

    if getattr(panel, 'bl_category', None):
        return panel.bl_category

    return 'Misc'


def is_excluded(panel: bpy.types.Panel) -> bool:
    prefs = utils.addon.prefs()
    exclude = [tab.strip() for tab in prefs.exclude_tabs.split(',')]
    return tab(panel) in exclude


def module(panel: bpy.types.Panel) -> str:
    return inspect.getmodule(panel).__name__.split('.')[0]


def is_special(panel: bpy.types.Panel) -> bool:
    special = {
        utils.hops.get_module(),
        utils.bc.get_module(),
    }

    return module(panel) in special


def is_registered(panel: bpy.types.Panel) -> bool:
    if getattr(panel, 'bl_idname', None):
        name = panel.bl_idname
    else:
        name = panel.__name__

    return hasattr(bpy.types, name)


def poll(panel: bpy.types.Panel) -> bool:
    if hasattr(panel, 'poll'):
        try:
            if not panel.poll(bpy.context):
                return False
        except:
            return False

    return True


def check(panel: bpy.types.Panel) -> bool:
    if getattr(panel, 'bl_parent_id', None):
        parent = getattr(bpy.types, panel.bl_parent_id, None)

        if parent and not check(parent):
            return False

    if getattr(panel, 'bl_space_type', None) != 'VIEW_3D':
        return False

    if getattr(panel, 'bl_region_type', None) != 'UI':
        return False

    if is_excluded(panel):
        return False

    if is_special(panel):
        return False

    if not is_registered(panel):
        return False

    if module(panel) != 'bl_ui':
        if not poll(panel):
            return False

    return True


def panels() -> list:
    panels = []

    def find_subclasses(a):
        for b in a.__subclasses__():
            if check(b):
                panels.append(b)

            for c in b.__subclasses__():
                find_subclasses(c)

    find_subclasses(bpy.types.Panel)

    return panels


def tabs() -> set:
    tabs = set()

    for panel in panels():
        tabs.add(tab(panel))

    return tabs


def update(panel: bpy.types.Panel):
    try:
        bpy.utils.unregister_class(panel)
    except:
        print('-' * 50)
        print(f'Failed to unregister {panel}')
        traceback.print_exc()
        print('-' * 50)
        return

    try:
        bpy.utils.register_class(panel)
    except:
        print('-' * 50)
        print(f'Failed to register {panel}')
        traceback.print_exc()
        print('-' * 50)
