from odoo import api, models

from ..models.report_helper import QWebHelper


class RuInvoiceReport(models.AbstractModel):
    _name = "report.l10n_ru_doc.report_invoice"

    @api.multi
    def get_report_values(self, docids, data=None):
        docs = self.env["account.invoice"].browse(docids)
        return {
            "helper": QWebHelper(),
            "doc_ids": docs.ids,
            "doc_model": "account.invoice",
            "docs": docs,
        }
