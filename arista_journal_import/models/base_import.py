from odoo import api, models

class BaseImportImport(models.TransientModel):
    _inherit = 'base_import.import'

    @api.model
    def get_fields_tree(self, model, depth=3):
        if model == 'account.journal':
            self = self.with_context(
                _journal_import_company_field=True
            )
        return super().get_fields_tree(model, depth=depth)