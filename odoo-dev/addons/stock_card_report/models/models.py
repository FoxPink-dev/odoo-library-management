# from odoo import models, fields, api


# class stock_card_report(models.Model):
#     _name = 'stock_card_report.stock_card_report'
#     _description = 'stock_card_report.stock_card_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

