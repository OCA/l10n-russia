from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    kpp = fields.Char("KPP", size=9)
    okpo = fields.Char("OKPO", size=14)
