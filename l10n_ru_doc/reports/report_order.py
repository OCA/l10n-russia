from odoo import api, models

from ..models.report_helper import QWebHelper


class RuSaleOrderReport(models.AbstractModel):
    _name = "report.l10n_ru_doc.report_order"

    @api.multi
    def get_report_values(self, docids, data=None):
        docs = self.env["sale.order"].browse(docids)
        return {
            "helper": QWebHelper(),
            "doc_ids": docs.ids,
            "doc_model": "sale.order",
            "docs": docs,
        }
