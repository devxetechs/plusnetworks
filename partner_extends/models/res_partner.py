# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zone = fields.Char(string="Zone")
    municipality_id = fields.Many2one("res.country.municipality", string="Municipality")
    speed = fields.Char(string="Bandwidth")
    ip_assigned = fields.Char(string="Assigned Public IP")

    link_code = fields.Char(string="Link Code")
    annex_code = fields.Char(string="Annex code")
    att_expiration_date = fields.Date(string='Attachment Expiration Date', store=True, default=fields.Datetime.now)
    
    economic_sector = fields.Many2one("economic.sector", string="Sector Económico")
    activation_date = fields.Date(string='Fecha de Activación en Contacto', store=True, default=fields.Datetime.now)
    link_state = fields.Selection([
        ('deactivated', 'Desactivado'), 
        ('activated', 'Activado'), 
        ('suspended', 'Suspendido'),
        ('legal', 'Legal'),
        ('cancel', 'Cancelado')], string='Estado del Enlace', copy=False, default='deactivated', required=True)

    def name_get(self):
        self.browse(self.ids).read(['name'])
        return [(template.id, '%s' % (template.name))
                for template in self]
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = args + [('name', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    
    def button_activate(self):
        self.write({'link_state': 'activated'})
        self.activation_date = datetime.now().today()
    
    def button_legal(self):
        self.write({'link_state': 'legal'})
        
    def button_suspended(self):
        self.write({'link_state': 'suspended'})
    
    def button_cancel(self):
        self.write({'link_state': 'cancel'})