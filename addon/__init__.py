from . import utils
from . import props
from . import icons
from . import ops
from . import ui


modules = (
    utils,
    props,
    icons,
    ops,
    ui,
)


def register():
    for module in modules:
        module.register()

    import bpy

    def timer():
        bpy.ops.simpletabs.update()

    bpy.app.timers.register(timer, first_interval=5)


def unregister():
    for module in reversed(modules):
        module.unregister()
