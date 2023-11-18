from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    kpp = fields.Char(related="partner_id.kpp")
    okpo = fields.Char(related="partner_id.okpo")
    chief_id = fields.Many2one("res.users", "Chief")
    accountant_id = fields.Many2one("res.users", "General Accountant")
    print_facsimile = fields.Boolean(
        "Print Facsimile",
        help="Check this for adding Facsimiles of responsible persons to documents.",
    )
    print_stamp = fields.Boolean(
        "Print Stamp", help="Check this for adding Stamp of company to documents."
    )
    stamp = fields.Binary("Stamp")
    print_anywhere = fields.Boolean(
        "Print Anywhere",
        help="Uncheck this, if you want add Facsimile and Stamp only in email.",
        default=True,
    )
