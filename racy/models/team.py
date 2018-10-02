# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Team(models.Model):
    _name = 'racy.team'
    _order = 'team_number'

    @api.model
    def _get_default_route(self):
        if self.race_id:
            if len(self.race_id.route_ids) == 1:
                return self.race_id.route_ids[0]

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
    team_number = fields.Integer(string="Number")
    category_id = fields.Many2one('racy.category', string='Category')
    group_id = fields.Many2one('racy.group', string='Group')
    route_id = fields.Many2one('racy.route', string="Route", default=lambda self: self._get_default_route(), required=True)
    group_mode = fields.Selection(related='race_id.group_mode', string="Racing mode")

    lap_ids = fields.One2many('racy.lap', 'race_id', string="Laps")
    lap_count = fields.Integer(string="Laps count", compute='_compute_lap_count')

    @api.one
    def _compute_lap_count(self):
        self.lap_count = len(self.lap_ids)
