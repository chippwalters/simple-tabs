import bpy
from . import startup
from .. import utils
from bpy.app.handlers import persistent

@persistent
def load_handler(_):
    prefs = utils.addon.prefs()
    bpy.app.timers.register(startup.startup_timer, first_interval=prefs.startup_delay)

def register():
    prefs = utils.addon.prefs()

    if not bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.register(startup.startup_timer, first_interval=prefs.startup_delay)

    bpy.app.handlers.load_post.append(load_handler)

def unregister():
    if bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.unregister(startup.startup_timer)

    bpy.app.handlers.load_post.remove(load_handler)
