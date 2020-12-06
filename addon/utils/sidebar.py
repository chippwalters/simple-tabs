import bpy


def panels() -> set:
    panels = set()

    for panel in bpy.types.Panel.__subclasses__():
        if getattr(panel, 'bl_space_type', None) != 'VIEW_3D':
            continue

        if getattr(panel, 'bl_region_type', None) != 'UI':
            continue

        if hasattr(panel, 'poll'):
            try:
                if not panel.poll(bpy.context):
                    continue
            except:
                continue

        if hasattr(panel, 'bl_category'):
            panels.add(panel)

    return panels


def categories() -> set:
    categories = set()

    for panel in panels():
        if panel.bl_category:
            categories.add(panel.bl_category)
        else:
            categories.add('Misc')

    return categories


def update(panel: bpy.types.Panel):
    try:
        bpy.utils.unregister_class(panel)
        bpy.utils.register_class(panel)
    except:
        pass
