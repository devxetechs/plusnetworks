# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from datetime import datetime, date, timedelta
from odoo import api, fields, models, _

                
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    partner_ref = fields.Char(string="Reference", store=True)
    
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for order in self:
            if order.partner_id:
                order.partner_ref = order.partner_id.ref
                
    
    