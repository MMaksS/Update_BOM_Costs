# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
import odoo.addons.decimal_precision as dp
from odoo.osv import expression

class ProductProduct(models.Model):
    _inherit = "product.template"
    
    
    @api.multi
    def _compute_cost_from_bom(self):
        bom_obj = self.env['mrp.bom']
        for p in self:
            search_bom_product = bom_obj.search([('product_tmpl_id', '=', p.id)], limit=1, order="id desc")
            if search_bom_product:
                cost = 0.0
                for bom in search_bom_product:
                    if bom.bom_line_ids:
                        for line in bom.bom_line_ids:
                            if line.product_id.cost_price_bom > 0.0:
                                product_cost = line.product_id.cost_price_bom
                            else:
                                product_cost = line.product_id.standard_price
                            product_qty = line.product_qty
                            cost += (product_qty/bom.product_qty * product_cost)
                        p.cost_price_bom = cost

    cost_price_bom = fields.Float(
        'Cost Incl. BOM', compute='_compute_cost_from_bom',
        digits=dp.get_precision('Product Price'),
        groups="base.group_user")

class MrpBom(models.Model):
    _inherit = "mrp.bom"
    
    @api.multi
    def _compute_mrp_total_cost(self):
        total = 0.0
        for line in self.bom_line_ids:
            total += line.total_cost
            self.total_bom_cost = total/self.product_qty
            
    total_bom_cost = fields.Float(compute='_compute_mrp_total_cost',string='Total BOM Cost For 1 Quantity')

class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"
        
    def _compute_cost_price(self):
        for bom_line in self:
            res = {}
            if not bom_line.product_id:
                return res
            if bom_line.product_id.cost_price_bom == 0.0:
                bom_line.cost = bom_line.product_id.standard_price
            else:
                bom_line.cost = bom_line.product_id.cost_price_bom
        
    @api.onchange('product_qty', 'cost')
    def _compute_mrp_line_total_cost(self):
        total = 0.0
        for line in self:
            total = (line.product_qty/line.bom_id.product_qty * line.cost)
            line.total_cost = total
            
    cost = fields.Float(compute='_compute_cost_price',string='Cost')
    total_cost = fields.Float(compute='_compute_mrp_line_total_cost',string='Total Cost',default=0.0)
    
                

