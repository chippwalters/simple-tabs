import bpy
from . import refresh
from . import update
from . import add
from . import remove
from . import move
from . import export_settings
from . import import_settings


classes = (
    refresh.Refresh,
    update.Update,
    add.Add,
    remove.Remove,
    move.Move,
    export_settings.ExportSettings,
    import_settings.ImportSettings,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
