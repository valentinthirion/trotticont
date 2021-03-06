# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class Route(models.Model):
    _name = 'racy.route'
    _order = 'race_id'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
    length = fields.Float(string="Length (km)", default=0.0)
    d_plus = fields.Float(strig="D+", default=0.0)
    start_date = fields.Datetime(string="Planned Start")
    end_date = fields.Datetime(string="Planned End")
    start_date_real = fields.Datetime(string="Start real")

    racer_count = fields.Integer(string="Racer count", compute='_compute_racer_count')
    team_count = fields.Integer(string="Team count", compute='_compute_team_count')
    lap_count = fields.Integer(string="Lap(s) count", compute='_compute_lap_count')

    racing_mode = fields.Selection(related='race_id.racing_mode', string="Racing mode")

    @api.one
    def _compute_lap_count(self):
        self.lap_count = len(self.env['racy.lap'].search([('route_id', '=', self.id)]))

    @api.one
    def _compute_racer_count(self):
        self.racer_count = len(self.env['racy.racer'].search([('route_id', '=', self.id)]))

    @api.one
    def _compute_team_count(self):
        self.racer_count = len(self.env['racy.team'].search([('route_id', '=', self.id),]))

    @api.multi
    def init_route(self):
        for route in self:
            route.start_date_real = datetime.now()
