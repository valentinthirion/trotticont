# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Team(models.Model):
    _name = 'racy.team'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
    team_number = fields.Integer(string="Number")
    category_id = fields.Many2one('racy.team_category', string='Category')
    group_id = fields.Many2one('racy.team_group', string='Group')
    lap_ids = fields.One2many('racy.lap', 'team_id', string="Laps")
