import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-l10n-russia",
    description="Meta package for oca-l10n-russia Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-l10n_ru',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
