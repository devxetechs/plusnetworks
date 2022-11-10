# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zone = fields.Char(string="Zone")
    municipality_id = fields.Many2one("res.country.municipality", string="Municipality")

    speed = fields.Char(string="Speed")
    link_code = fields.Char(string="Link Code")
    annex_code = fields.Char(string="Annex code")
    att_expiration_date = fields.Date(string='Attachment Expiration Date', store=True, default=fields.Datetime.now)