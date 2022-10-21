# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class ResCountryMunicipality(models.Model):
    _name = 'res.country.municipality'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    region = fields.Many2one('res.country.region', 'Region')
    state_id = fields.Many2one("res.country.state", string="Department")
