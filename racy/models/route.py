# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Route(models.Model):
    _name = 'racy.route'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
    length = fields.Float(string="Length (km)", default=0.0)
    d_plus = fields.Float(strig="D+", default=0.0)
    start_date = fields.Datetime(string="Start")
    end_date = fields.Datetime(string="End")
