from odoo import models, fields, api


class StockCardWizard(models.TransientModel):
    _name = 'stock.card.wizard'
    _description = 'Stock Card Report Wizard'

    date_from = fields.Date(string='From Date', required=True)
    date_to = fields.Date(string='To Date', required=True)
    product_ids = fields.Many2many('product.product', string='Products')
    category_id = fields.Many2one('product.category', string='Product Category')
    warehouse_ids = fields.Many2many('stock.warehouse', string='Warehouses')
    location_ids = fields.Many2many('stock.location', string='Locations')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    def action_generate_report(self):
        self.ensure_one()
        report_lines = self._compute_report_data()

        existing = self.env['stock.card.report.line'].search([('wizard_id', '=', self.id)])
        existing.unlink()

        line_vals = []
        for line in report_lines:
            line_vals.append({
                'wizard_id': self.id,
                'product_id': line['product_id'],
                'location_id': line.get('location_id'),
                'date': line['date'],
                'reference': line.get('reference', ''),
                'description': line.get('description', ''),
                'incoming_qty': line.get('incoming_qty', 0.0),
                'outgoing_qty': line.get('outgoing_qty', 0.0),
                'balance_qty': line.get('balance_qty', 0.0),
                'unit_cost': line.get('unit_cost', 0.0),
                'incoming_value': line.get('incoming_value', 0.0),
                'outgoing_value': line.get('outgoing_value', 0.0),
                'balance_value': line.get('balance_value', 0.0),
            })

        if line_vals:
            self.env['stock.card.report.line'].create(line_vals)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Stock Card Report',
            'res_model': 'stock.card.report.line',
            'view_mode': 'tree,graph,pivot',
            'domain': [('wizard_id', '=', self.id)],
            'target': 'main',
            'context': {
                'wizard_id': self.id,
                'search_default_group_by_product': True,
            },
        }

    def action_print_pdf(self):
        self.ensure_one()
        self.action_generate_report()
        return self.env.ref('stock_card_report.action_report_stock_card').report_action(self)

    def _compute_report_data(self):
        self.ensure_one()
        domain = [('state', '=', 'done')]
        if self.date_from:
            domain.append(('date', '>=', self.date_from))
        if self.date_to:
            domain.append(('date', '<=', self.date_to))
        if self.product_ids:
            domain.append(('product_id', 'in', self.product_ids.ids))
        if self.category_id:
            domain.append(('product_id.categ_id', '=', self.category_id.id))
        if self.location_ids:
            domain.append('|')
            domain.append(('location_id', 'in', self.location_ids.ids))
            domain.append(('location_dest_id', 'in', self.location_ids.ids))

        moves = self.env['stock.move'].search(domain, order='date, id')

        product_balance = {}
        lines = []

        for move in moves:
            product = move.product_id
            if not product:
                continue

            if product.id not in product_balance:
                opening = self._get_opening_balance(product, move.location_id)
                product_balance[product.id] = opening

            if move.location_dest_id.usage in ['internal', 'production'] \
                    and move.location_id.usage != 'internal':
                in_qty = move.product_uom_qty
                out_qty = 0.0
            elif move.location_id.usage in ['internal', 'production'] \
                    and move.location_dest_id.usage != 'internal':
                in_qty = 0.0
                out_qty = move.product_uom_qty
            else:
                continue

            product_balance[product.id] += in_qty - out_qty
            unit_cost = move.price_unit or product.standard_price

            lines.append({
                'product_id': product.id,
                'location_id': move.location_id.id or move.location_dest_id.id,
                'date': move.date,
                'reference': move.picking_id.name or move.origin or '',
                'description': move.reference or product.display_name,
                'incoming_qty': in_qty,
                'outgoing_qty': out_qty,
                'balance_qty': product_balance[product.id],
                'unit_cost': unit_cost,
                'incoming_value': in_qty * unit_cost,
                'outgoing_value': out_qty * unit_cost,
                'balance_value': product_balance[product.id] * unit_cost,
            })

        return lines

    def _get_opening_balance(self, product, location):
        domain = [
            ('product_id', '=', product.id),
            ('state', '=', 'done'),
            ('date', '<', self.date_from),
        ]
        if self.location_ids:
            domain.append('|')
            domain.append(('location_id', 'in', self.location_ids.ids))
            domain.append(('location_dest_id', 'in', self.location_ids.ids))

        prior_moves = self.env['stock.move'].search(domain, order='date, id')
        balance = 0.0
        for move in prior_moves:
            if move.location_dest_id.usage in ['internal', 'production'] \
                    and move.location_id.usage != 'internal':
                balance += move.product_uom_qty
            elif move.location_id.usage in ['internal', 'production'] \
                    and move.location_dest_id.usage != 'internal':
                balance -= move.product_uom_qty
        return balance


class StockCardReportLine(models.TransientModel):
    _name = 'stock.card.report.line'
    _description = 'Stock Card Report Line'
    _order = 'product_id, date'

    wizard_id = fields.Many2one('stock.card.wizard', string='Wizard', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    location_id = fields.Many2one('stock.location', string='Location')
    date = fields.Datetime(string='Date')
    reference = fields.Char(string='Reference')
    description = fields.Char(string='Description')
    incoming_qty = fields.Float(string='Incoming Qty', digits='Product Unit of Measure')
    outgoing_qty = fields.Float(string='Outgoing Qty', digits='Product Unit of Measure')
    balance_qty = fields.Float(string='Balance Qty', digits='Product Unit of Measure')
    unit_cost = fields.Float(string='Unit Cost', digits='Product Price')
    incoming_value = fields.Float(string='Incoming Value', digits='Product Price')
    outgoing_value = fields.Float(string='Outgoing Value', digits='Product Price')
    balance_value = fields.Float(string='Balance Value', digits='Product Price')
