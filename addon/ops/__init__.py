import bpy
from . import refresh
from . import move
from . import update


classes = (
    refresh.Refresh,
    move.Move,
    update.Update,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
