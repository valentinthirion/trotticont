# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
from openerp import tools, _

import logging
_logger = logging.getLogger(__name__)

class Race(models.Model):
    _name = 'racy.race'
    _order = 'date desc'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    place = fields.Char(string='Place', copy=False)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ended', 'Ended'),
        ('cancel', 'Cancelled')
    ], string='State', default='draft', required=True)
    date = fields.Datetime(string='Date', required=True)

    image = fields.Binary("Photo", attachment=True)
    image_medium = fields.Binary("Medium-sized photo", attachment=True)
    image_small = fields.Binary("Small-sized photo", attachment=True)

    route_ids = fields.One2many('racy.route', 'race_id', string="Routes")
    route_count = fields.Integer(string="Routes count", compute='_compute_route_count')
    team_ids = fields.One2many('racy.team', 'race_id', string='Teams')
    team_count = fields.Integer(string="Teams count", compute='_compute_team_count')
    racer_ids = fields.One2many('racy.racer', 'race_id', string="Racers")
    racer_count = fields.Integer(string="Racer count", compute='_compute_racer_count')

    racing_mode = fields.Selection([('single', 'Single'), ('team', 'Team race')], string="Racing mode", default='single')
    group_mode = fields.Selection([('category', 'By Categories'), ('superteam', 'By Groups of Teams')], string="Racing mode", default='category')

    category_ids = fields.One2many('racy.category', 'race_id', string="Categories of teams")
    group_ids = fields.One2many('racy.group', 'race_id', string="Groups of teams")

    @api.one
    def _compute_route_count(self):
        self.route_count = len(self.route_ids)

    @api.one
    def _compute_team_count(self):
        self.team_count = len(self.team_ids)

    @api.one
    def _compute_racer_count(self):
        self.racer_count = len(self.racer_ids)

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Race, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Race, self).write(vals)
