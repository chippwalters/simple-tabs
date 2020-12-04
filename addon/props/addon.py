import bpy
from .. import utils


class AddonProps(bpy.types.PropertyGroup):
    @property
    def module(self) -> str:
        return utils.addon.module()


    @property
    def prefs(self) -> bpy.types.AddonPreferences:
        return utils.addon.prefs()
