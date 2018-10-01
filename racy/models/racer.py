# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Racer(models.Model):
    _name = 'racy.racer'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
    number = fields.Integer(string="Number")
    category_id = fields.Many2one('racy.team_category', string='Category')
    partner_id = fields.Many2one('res.partner', string="Contact")
    lap_ids = fields.One2many('racy.lap', 'racer_id', string="Laps")