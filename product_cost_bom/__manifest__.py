# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Update Product Cost from BOM',
    'version': '11.0.0.5',
    'category': 'Manufacturing',
    "summary": """
       Module help to show Cost Price inculded BOM which calculate from cost of All componant of Bill of Material.""",
    'author': 'BrowseInfo',
    'description': """
    Module use for calculate product cost from BOM, Calculate cost from Bill of Material, Calculate product cost from bill of material, calculate cost form subassembly. Module help to show Cost Price inculded BOM which calculate from cost of All componant of Bill of Material, Product subassembly, subassembly costing, subassembly product cost.BOM COST on product.
""",
    "price": 30,
    "currency": 'EUR',
    'website': 'http://www.browseinfo.in',
    'depends': ['base','product','mrp','sale_management'],
    'data': ['views/product_view.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
