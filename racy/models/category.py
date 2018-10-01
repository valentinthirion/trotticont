# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Category(models.Model):
    _name = 'racy.category'

    name = fields.Char(string='Name', copy=False, index=True, required=True)
    race_id = fields.Many2one('racy.race', string='Race', required=True)
