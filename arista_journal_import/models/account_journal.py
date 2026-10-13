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

    @api.model_create_multi
    def create(self, vals_list):
        # Jika sedang dalam proses import dan ada company_id yang berbeda,
        # pastikan user diizinkan membuat record untuk company tersebut.
        if self.env.context.get('_journal_import_company_field') or self.env.context.get('import_file'):
            company_ids = [vals.get('company_id') for vals in vals_list if vals.get('company_id')]
            if company_ids:
                # Tambahkan company tersebut ke allowed_company_ids di environment sementara
                allowed = set(self.env.context.get('allowed_company_ids', []))
                allowed.update(company_ids)
                self = self.with_context(allowed_company_ids=list(allowed))
                
        return super().create(vals_list)