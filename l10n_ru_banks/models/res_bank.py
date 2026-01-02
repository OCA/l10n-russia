from odoo import fields, models


class ResBank(models.Model):
    _inherit = "res.bank"
    _description = "Russian Banks"

    corr_acc = fields.Char('Corresponding account', size=64)