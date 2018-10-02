# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Group(models.Model):
    _name = 'racy.group'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)

    team_count = fields.Integer(string="Team count", compute='_compute_team_count')

    @api.one
    def _compute_team_count(self):
        self.team_count = len(self.env['racy.team'].search([('group_id', '=', self.id)]))
