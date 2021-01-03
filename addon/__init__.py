from . import utils
from . import props
from . import icons
from . import ops
from . import ui
from . import timers


modules = (
    utils,
    props,
    icons,
    ops,
    ui,
    timers,
)


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
