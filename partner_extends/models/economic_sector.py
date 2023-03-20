# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class EconomicSector(models.Model):
    _name = 'economic.sector'

    name = fields.Char(string="Nombre")