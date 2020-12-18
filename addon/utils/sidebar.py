import bpy


mode_table = {
    'EDIT_MESH': 'mesh_edit',
    'EDIT_CURVE': 'curve_edit',
    'EDIT_SURFACE': 'surface_edit',
    'EDIT_TEXT': 'text_edit',
    'EDIT_ARMATURE': 'armature_edit',
    'EDIT_METABALL': 'mball_edit',
    'LATTICE_EDIT': 'lattice_edit',
    'POSE': 'posemode',
    'SCULPT': 'sculpt_mode',
    'PAINT_WEIGHT': 'weightpaint',
    'PAINT_VERTEX': 'vertexpaint',
    'PAINT_TEXTURE': 'imagepaint',
    'PARTICLE': 'particlemode',
    'OBJECT': 'objectmode',
    'PAINT_GPENCIL': 'greasepencil_paint',
    'EDIT_GPENCIL': 'greasepencil_edit',
    'SCULPT_GPENCIL': 'greasepencil_sculpt',
    'WEIGHT_GPENCIL': 'greasepencil_weight',
    'VERTEX_GPENCIL': 'greasepencil_vertex',
}


def check(panel: bpy.types.Panel) -> bool:
    if getattr(panel, 'bl_category', None) == 'Item':
        return False

    if getattr(panel, 'bl_space_type', None) != 'VIEW_3D':
        return False

    if getattr(panel, 'bl_region_type', None) != 'UI':
        return False

    if getattr(panel, 'bl_context', None):
        bl_context = panel.bl_context.replace('.', '')
        if bl_context != mode_table[bpy.context.mode]:
            return False

    if hasattr(panel, 'poll'):
        try:
            if not panel.poll(bpy.context):
                return False
        except:
            return False

    return True


def panels() -> list:
    panels = []

    for panel in bpy.types.Panel.__subclasses__():
        if check(panel):
            panels.append(panel)

    return panels


def tab(panel: bpy.types.Panel) -> str:
    if getattr(panel, 'original_category', None):
        return panel.original_category
    elif getattr(panel, 'bl_category', None):
        return panel.bl_category
    else:
        return 'Misc'


def tabs() -> set:
    tabs = set()

    for panel in panels():
        tabs.add(tab(panel))

    return tabs


def update(panel: bpy.types.Panel):
    try:
        bpy.utils.unregister_class(panel)
        bpy.utils.register_class(panel)
    except:
        pass
