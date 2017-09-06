# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Team(models.Model):
    _name = 'trotticont.team'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('trotticont.race', string='Race', required=True)
    team_number = fields.Integer(string="Number")
    category_id = fields.Many2one('trotticont.race_category', string="Category")
    group_id = fields.Many2one('trotticont.race_group', string="Group")
