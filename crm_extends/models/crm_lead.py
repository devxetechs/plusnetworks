# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from datetime import datetime, date, timedelta
from odoo import api, fields, models, _


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    arc = fields.Float(string="ARC", store=True, compute="_compute_arc")
    partner_ref = fields.Char(string="Reference", store=True)
    months_numbers = fields.Float(string="Months Number")
    
    @api.depends('months_numbers', 'expected_revenue')
    def _compute_arc(self):
        for order in self:
            arc = (order.months_numbers * order.expected_revenue) if order.months_numbers > 0.00 and order.expected_revenue > 0.00 else 0.00
            order.arc = arc
    
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for order in self:
            if order.partner_id:
                order.partner_ref = order.partner_id.ref