# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
from datetime import date, datetime
import logging

_logger = logging.getLogger(__name__)


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    date_opening = fields.Datetime(string="Opening date and time", copy=False, default=datetime.now())
    date_incidence = fields.Datetime(string="Incidence date and time", copy=False, default=datetime.now())
    date_established = fields.Datetime(string="Established date and time", copy=False, default=datetime.now())

    speed = fields.Char(string="Speed", store=True)
    link_code = fields.Char(string="Link Code", store=True)
    partner_ref = fields.Char(string="Reference", store=True)
    annex_code = fields.Char(string="Código anexo", store=True)
    
    stage_name = fields.Char(string="Stage Name", store=True, related="stage_id.name")
    
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for order in self:
            if order.partner_id:
                order.annex_code = order.partner_id.annex_code
                order.partner_ref = order.partner_id.ref
                order.link_code = order.partner_id.link_code
                order.speed = order.partner_id.speed