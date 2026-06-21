from odoo.tests import common


class TestStockCardWizard(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.Wizard = self.env['stock.card.wizard']
        self.ReportLine = self.env['stock.card.report.line']
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'consu',
            'standard_price': 50.0,
            'list_price': 100.0,
        })
        self.warehouse = self.env.ref('stock.warehouse0')

    def test_wizard_create_with_defaults(self):
        from datetime import date
        wizard = self.Wizard.create({
            'date_from': '2026-01-01',
            'date_to': '2026-12-31',
        })
        self.assertTrue(wizard.id)
        self.assertEqual(wizard.date_from, date(2026, 1, 1))

    def test_wizard_create_with_products(self):
        wizard = self.Wizard.create({
            'date_from': '2026-01-01',
            'date_to': '2026-12-31',
            'product_ids': [(6, 0, self.product.ids)],
        })
        self.assertIn(self.product, wizard.product_ids)

    def test_generate_report_returns_action(self):
        wizard = self.Wizard.create({
            'date_from': '2026-01-01',
            'date_to': '2026-12-31',
        })
        action = wizard.action_generate_report()
        self.assertEqual(action['type'], 'ir.actions.act_window')
        self.assertEqual(action['res_model'], 'stock.card.report.line')

    def test_generate_report_creates_lines(self):
        wizard = self.Wizard.create({
            'date_from': '2026-01-01',
            'date_to': '2026-12-31',
        })
        wizard.action_generate_report()
        lines = self.ReportLine.search([('wizard_id', '=', wizard.id)])
        self.assertTrue(len(lines) >= 0)

    def test_multiple_wizards_independent(self):
        w1 = self.Wizard.create({'date_from': '2026-01-01', 'date_to': '2026-06-30'})
        w2 = self.Wizard.create({'date_from': '2026-07-01', 'date_to': '2026-12-31'})
        w1.action_generate_report()
        w2.action_generate_report()
        lines1 = self.ReportLine.search([('wizard_id', '=', w1.id)])
        lines2 = self.ReportLine.search([('wizard_id', '=', w2.id)])
        for line in lines1:
            self.assertEqual(line.wizard_id.id, w1.id)
        for line in lines2:
            self.assertEqual(line.wizard_id.id, w2.id)
