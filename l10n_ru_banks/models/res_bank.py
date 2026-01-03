from odoo import api, fields, models


class ResBank(models.Model):
    _inherit = "res.bank"
    _description = "Russian Banks"

    corr_acc = fields.Char(
        "Correspondent account", help="Correspondent account used by Russian banks"
    )

    country_code = fields.Char(related="country.code", store=False)


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    bank_corr_acc = fields.Char(
        "Correspondent account", help="Correspondent account used by Russian banks"
    )

    @api.onchange("bank_id")
    def onchange_bank_id(self):
        self.bank_name = self.bank_id.name
        self.bank_bic = self.bank_id.bic
        self.bank_corr_acc = self.bank_id.corr_acc
