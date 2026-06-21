from odoo.tests import common


class TestStockCardReportLine(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.Wizard = self.env['stock.card.wizard']
        self.ReportLine = self.env['stock.card.report.line']
        self.wizard = self.Wizard.create({
            'date_from': '2026-01-01',
            'date_to': '2026-12-31',
        })

    def test_report_line_creation(self):
        self.wizard.action_generate_report()
        lines = self.ReportLine.search([('wizard_id', '=', self.wizard.id)])
        for line in lines:
            self.assertTrue(line.product_id)
            self.assertTrue(line.date)
            self.assertTrue(line.balance_qty is not None)

    def test_report_line_valuation_fields(self):
        self.wizard.action_generate_report()
        lines = self.ReportLine.search([('wizard_id', '=', self.wizard.id)])
        for line in lines:
            self.assertTrue(line.unit_cost >= 0)
            self.assertTrue(line.incoming_value >= 0)
            self.assertTrue(line.outgoing_value >= 0)

    def test_report_line_balance_consistency(self):
        self.wizard.action_generate_report()
        lines = self.ReportLine.search(
            [('wizard_id', '=', self.wizard.id)],
            order='product_id, date'
        )
        products = lines.mapped('product_id')
        for product in products:
            product_lines = lines.filtered(lambda l: l.product_id == product)
            balance = 0.0
            for line in product_lines:
                balance += line.incoming_qty - line.outgoing_qty
                self.assertAlmostEqual(line.balance_qty, balance, places=2)

    def test_report_line_delete_on_wizard_cleanup(self):
        self.wizard.action_generate_report()
        line_count = self.ReportLine.search_count([('wizard_id', '=', self.wizard.id)])
        self.assertTrue(line_count > 0)
        self.wizard.unlink()
        old_lines = self.ReportLine.search([('wizard_id', '=', self.wizard.id)])
        self.assertEqual(len(old_lines), 0)

    def test_negative_filter(self):
        wiz = self.Wizard.create({
            'date_from': '2099-01-01',
            'date_to': '2099-12-31',
        })
        wiz.action_generate_report()
        lines = self.ReportLine.search([('wizard_id', '=', wiz.id)])
        self.assertEqual(len(lines), 0)
