
from odoo import api, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        result = super().fields_get(
            allfields=allfields,
            attributes=attributes,
        )

        if (
            self.env.context.get('_journal_import_company_field')
            and 'company_id' in result
        ):
            result['company_id']['readonly'] = False

        return result
