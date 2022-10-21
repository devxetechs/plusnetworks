# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zone = fields.Char(string="Zone")
    municipality_id = fields.Many2one("res.country.municipality", string="Municipality")
