# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError, UserError, ValidationError
from odoo import api, fields, models, _, SUPERUSER_ID
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
# import logging
#
# _logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    annex_code = fields.Char(string="Annex code", readonly=True, copy=False)
    @api.model
    def create(self, vals):
        if not vals.get('annex_code') or vals['annex_code'] == False:
            vals['annex_code'] = self.env['ir.sequence'].next_by_code('res.partner')
        return super(ResPartner, self).create(vals)
