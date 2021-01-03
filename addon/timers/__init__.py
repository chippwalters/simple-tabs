import bpy
from . import startup
from .. import utils


def register():
    prefs = utils.addon.prefs()

    if not bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.register(startup.startup_timer, first_interval=prefs.startup_delay)


def unregister():
    if bpy.app.timers.is_registered(startup.startup_timer):
        bpy.app.timers.unregister(startup.startup_timer)
