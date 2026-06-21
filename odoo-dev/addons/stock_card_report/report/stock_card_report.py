from odoo import models


class ReportStockCard(models.AbstractModel):
    _name = 'report.stock_card_report.report_stock_card'
    _description = 'Stock Card PDF Report'

    def _get_report_values(self, docids, data=None):
        wizard = self.env['stock.card.wizard'].browse(docids)
        wizard.action_generate_report()
        lines = self.env['stock.card.report.line'].search([('wizard_id', '=', wizard.id)])

        products = lines.mapped('product_id')
        product_data = []
        for product in products:
            product_lines = lines.filtered(lambda l: l.product_id == product)
            product_data.append({
                'product': product,
                'lines': product_lines,
                'total_in': sum(product_lines.mapped('incoming_qty')),
                'total_out': sum(product_lines.mapped('outgoing_qty')),
                'closing_balance': product_lines[-1].balance_qty if product_lines else 0.0,
            })

        return {
            'doc_ids': docids,
            'doc_model': 'stock.card.wizard',
            'docs': wizard,
            'product_data': product_data,
        }
