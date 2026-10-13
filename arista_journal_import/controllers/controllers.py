# -*- coding: utf-8 -*-
# from odoo import http


# class AristaJournalImport(http.Controller):
#     @http.route('/arista_journal_import/arista_journal_import', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arista_journal_import/arista_journal_import/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arista_journal_import.listing', {
#             'root': '/arista_journal_import/arista_journal_import',
#             'objects': http.request.env['arista_journal_import.arista_journal_import'].search([]),
#         })

#     @http.route('/arista_journal_import/arista_journal_import/objects/<model("arista_journal_import.arista_journal_import"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arista_journal_import.object', {
#             'object': obj
#         })

