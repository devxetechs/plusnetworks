# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class ResCountryRegion(models.Model):
    _name = 'res.country.region'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    