# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
from openerp import tools, _

import logging
_logger = logging.getLogger(__name__)

class Race(models.Model):
    _name = 'trotticont.race'
    _order = 'date desc'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('trotticont', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    name = fields.Char(string='Name', copy=False, index=True, required=True, readonly=True)
    place = fields.Char(string='Place', copy=False, index=True, required=True, readonly=True)
    description = fields.Text(string='Description', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ended', 'Ended'),
        ('cancel', 'Cancelled')
    ], string='State', default='draft', required=True)
    date = fields.Datetime(string='Date', required=True, readonly=True)
    lenght = fields.Float(string='Length')
    image = fields.Binary("Photo", default= _default_image, attachment=True)
    image_medium = fields.Binary("Medium-sized photo", attachment=True)
    image_small = fields.Binary("Small-sized photo", attachment=True)
    time_start = fields.Datetime(string='Race start', required=True, readonly=True)
    time_end = fields.Datetime(string='Race end', required=True, readonly=True)
    team_ids = fields.One2many('trotticont.team', 'race_id', string='Teams')
    team_count = fields.Integer(string="Teams count", compute='_compute_team_count')

    @api.one
    def _compute_team_count(self):
        self.team_count = len(self.team_ids)

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Race, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Race, self).write(vals)
