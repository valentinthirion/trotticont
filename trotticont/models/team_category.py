# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class TeamCategory(models.Model):
    _name = 'trotticont.team_category'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('trotticont.race', string='Race', required=True)
