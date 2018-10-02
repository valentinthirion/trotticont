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

    @api.one
    def name_get(self):
        if self.racer_id:
            return (self.id, self.racer_id.name + ' - ' + self.race_id.name + ' - ' + self.route_id.name + ' [' + self.create_date + ']')
        if self.team_id:
            return (self.id, self.team_id.name + ' - ' + self.race_id.name + ' - ' + self.route_id.name + ' [' + self.create_date + ']')