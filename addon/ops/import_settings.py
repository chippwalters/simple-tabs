import bpy
import bpy_extras
from .. import utils


class ImportSettings(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    bl_idname = 'simpletabs.import_settings'
    bl_label = 'Import Settings'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}
    bl_description = '.\n'.join((
        'Load addon preferences from a file',
        'Made possible by PowerBackup'))

    filter_glob: bpy.props.StringProperty(default='*.json', options={'HIDDEN'})
    filename_ext: bpy.props.StringProperty(default='.json', options={'HIDDEN'})

    def invoke(self, context, event):
        self.filepath = utils.backup.filepath()
        return super().invoke(context, event)

    def execute(self, context):
        result = utils.backup.restore(self.filepath)
        self.report(result[0], result[1])
        return result[2]
