from odoo import api, models


class BaseImportImport(models.Model):
    _inherit = 'base_import.import'

    @api.model
    def get_fields_tree(self, model, depth=3):
        if model == 'account.journal':
            self = self.with_context(
                _journal_import_company_field=True
            )
        return super().get_fields_tree(model, depth=depth)

    def execute_import(self, fields, columns, options, dryrun=False):
        """
        Override execute_import untuk memastikan saat import account.journal,
        system mengizinkan akses ke multi-company yang terlibat di dalam data excel.
        """
        res = super().execute_import(fields, columns, options, dryrun=dryrun)
        
        if self.res_model == 'account.journal':
            # Jika diperlukan tambahan penyesuaian context di sini
            pass
            
        return res