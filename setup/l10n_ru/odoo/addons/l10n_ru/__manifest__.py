# Copyright (C) 2013-2023 CodUP (<http://codup.com>)
# Copyright (C) 2023 Katulos (<http://github.com/Katulos>).
{
    "name": "Russia - Accounting",
    "version": "11.0.0.0.0",
    "summary": "This is the base module to manage the accounting chart for Russia in Odoo",
    "category": "Localization/Russia",
    "author": "CodUP, Katulos, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-russia",
    "license": "AGPL-3",
    "depends": ["account"],
    "demo": [],
    "data": [
        "data/account_chart.xml",
        "data/account.account.template.csv",
        "data/account_chart_template.xml",
        "data/account_tax_template.xml",
        "data/account_chart_template.yml",
    ],
    "installable": True,
}
