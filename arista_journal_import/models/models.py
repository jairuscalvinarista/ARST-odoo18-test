# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class arista_journal_import(models.Model):
#     _name = 'arista_journal_import.arista_journal_import'
#     _description = 'arista_journal_import.arista_journal_import'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

