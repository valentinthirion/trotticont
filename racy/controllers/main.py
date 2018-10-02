# -*- coding: utf-8 -*-
import logging
from openerp import http, _
from openerp.exceptions import AccessError
from openerp.http import request

_logger = logging.getLogger(__name__)


class RacyCountPage(http.Controller):

    @http.route([
        '/racy/race/<model("racy.race"):race>',
    ], type='http', auth="public", website=True)
    def racy_race_page(self, page=0, race=None, search='', ppg=False, **post):
        race_ids = http.request.env['racy.race'].sudo().search([('id', '=', race.id)])
        return http.request.render('racy.racy_race_count_page', {'race': race_ids})
