# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class TeamGroup(models.Model):
    _name = 'trotticont.team_group'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('trotticont.race', string='Race', required=True)
