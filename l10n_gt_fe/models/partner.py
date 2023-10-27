# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    country_id = fields.Many2one(default=lambda s: s.env.ref('base.gt'))

    @api.model_create_multi
    def create(self, vals_list):
        partners = super(ResPartner, self).create(vals_list)
        
        for vals in vals_list:
            if vals.get('vat') and self.company_type in ['company'] or vals.get('vat') and vals.get('company_type') in ['company']:
                vat_count = self.env["res.partner"].search_count([("vat", "=", vals.get('vat'))])
                
                if vat_count > 1:
                    raise ValidationError("Ya existe un contacto registrado con ese NIT, por favor ingresa otro.")
            
        return partners

    def write(self, vals):
        partners = super(ResPartner, self).write(vals)
        
        for partner in self:
        
            if vals.get('vat') and self.company_type in ['company'] or vals.get('vat') and vals.get('company_type') in ['company'] or self.vat and vals.get('company_type') in ['company']:
                vat_count = self.env["res.partner"].search_count([("vat", "=", vals.get('vat'))])

                if vat_count > 1:
                    raise ValidationError("Ya existe un contacto registrado con ese NIT, por favor ingresa otro.")
        
        return partners

    

    