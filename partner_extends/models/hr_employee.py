# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    state_id = fields.Many2one('res.country.state', related="address_id.state_id", string="Department")
    zone = fields.Char(related="address_id.zone", string="Zone")
    municipality_id = fields.Many2one("res.country.municipality", related="address_id.municipality_id", string="Municipality")
    code = fields.Char(related="address_id.municipality_id.code", string="Code")

    region = fields.Many2one('res.country.region', string='Region', related="address_id.municipality_id.region")
    igss = fields.Char(string="IGSS")
    vat = fields.Char(string="NIT")
    alter_code = fields.Char(string="Idioma (Código)")
