# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from datetime import datetime, date, timedelta
from odoo import api, fields, models, _


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    expected_revenue = fields.Monetary('MRC', currency_field='company_currency', tracking=True)