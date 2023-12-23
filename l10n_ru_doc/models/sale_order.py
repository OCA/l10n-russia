from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def print_quotation(self):
        self.filtered(lambda s: s.state == "draft").write({"state": "sent"})
        return {
            "type": "ir.actions.report",
            "report_name": "l10n_ru_doc.report_order",
            "report_type": "qweb-pdf",
        }
