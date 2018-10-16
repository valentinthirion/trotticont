# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
import datetime
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)

class Team(models.Model):
    _name = 'racy.team'
    _order = 'team_number'

    @api.model
    def _get_default_route(self):
        if self.race_id:
            if len(self.race_id.route_ids) == 1:
                return self.race_id.route_ids[0].id

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
    team_number = fields.Integer(string="Number")
    category_id = fields.Many2one('racy.category', string='Category')
    group_id = fields.Many2one('racy.group', string='Group')
    route_id = fields.Many2one('racy.route', string="Route", default=lambda self: self._get_default_route(), required=True)
    group_mode = fields.Selection(related='race_id.group_mode', string="Racing mode")

    lap_ids = fields.One2many('racy.lap', 'team_id', string="Laps")
    lap_count = fields.Integer(string="Laps count", compute='_compute_lap_count')

    avg_speed = fields.Float(string="Speed (km/h)", default=0.0, readonly=True)

    @api.one
    def _compute_lap_count(self):
        self.lap_count = len(self.lap_ids)

    @api.multi
    def addLap(self):
        for team in self:
            # Create the lap
            lap = self.env['racy.lap'].create({
                'race_id': team.race_id.id,
                'team_id': team.id,
                'route_id': team.route_id.id,
            })
            # Initiate the route
            if not team.route_id.start_date_real:
                team.route_id.start_date_real = fields.datetime.now()
            # Compute avg speed
            distance = team.route_id.length * team.lap_count
            datetimeFormat = '%Y-%m-%d %H:%M:%S'
            date_last_lap = datetime.datetime.strptime(lap.create_date, datetimeFormat)
            date_route_start = datetime.datetime.strptime(team.route_id.start_date_real,datetimeFormat)
            time_delta = date_last_lap - date_route_start
            team.avg_speed = float(distance / (float((time_delta.seconds)) / 3600))
