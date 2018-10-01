# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Lap(models.Model):
    _name = 'racy.lap'

    race_id = fields.Many2one('racy.race', string='Race', required=True)
    racer_id = fields.Many2one('racy.racer', string='Racer')
    team_id = fields.Many2one('racy.team', string='Team')
    route_id = fields.Many2one('racy.route', string='Route', required=True)