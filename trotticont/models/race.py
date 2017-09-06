# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Race(models.Model):
    _name = 'trotticont.race'
    _order = 'date desc'

    name = fields.Char(string='Name', copy=False, index=True, required=True, readonly=True, states={'draft': [('readonly', False)]})
    place = fields.Char(string='Place', copy=False, index=True, required=True, readonly=True, states={'draft': [('readonly', False)]})
    description = fields.Text(string='Description', readonly=True, states={'draft': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ended', 'Ended'),
        ('cancel', 'Cancelled')
    ], string='State', default='draft', required=True)
    date = fields.Datetime(string='Date', required=True, readonly=True, states={'draft': [('readonly', False)]})