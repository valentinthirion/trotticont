# -*- coding: utf-8 -*-
import logging
from openerp import http, _
from openerp.exceptions import AccessError
from openerp.http import request

_logger = logging.getLogger(__name__)


class RacyCountPage(http.Controller):

    @http.route([
        '/racy/race/<model("racy.race"):race_id>',
    ], type='http', auth="user", website=True)
    def racy_race_page(self, page=0, race_id=None, search='', ppg=False, **post):
        race_ids = http.request.env['racy.race'].sudo().search([('id', '=', race_id.id)])
        return http.request.render('racy.racy_race_count_page', {'race': race_ids})

    @http.route([
        '/racy/number_passed/validate_json'],
                type='json', auth="user", methods=['POST'], website=True, csrf=False)
    def number_passed_in_race(self, race_id, number, *kw):
        """ Ajax call to create a lap for a passed number """
        _logger.debug("\n\n HELLO WORLD !\n\n")
        # Test if team or racer
        if race_id and number:
            race = request.env['racy.race'].sudo().search([('id', '=', race_id)], limit=1)
            if race.racing_mode == 'single':
                racer = request.env['racy.racer'].sudo().search([
                    ('race_id', '=', race_id),
                    ('number', '=', int(number)),
                    ], limit=1)
                if not racer or len(racer) != 1:
                    return {
                        'racing_mode': 'single',
                        'racer_passed_id': -1
                    }
                else:
                    # Add one lap to this racer here + compute its avg speed and position
                    # Then return to the view
                    return {
                        'racing_mode': 'single',
                        'racer_passed_id': racer.id,
                        'racer_passed_number': racer.number,
                        'racer_passed_name': racer.name,
                    }
            elif race.racing_mode == 'team':
                team = request.env['racy.team'].sudo().search([
                    ('race_id', '=', race_id),
                    ('team_number', '=', int(number)),
                    ], limit=1)
                if not team or len(team) != 1:
                    return {
                        'racing_mode': 'team',
                        'team_passed_id': -1
                    }
                else:
                    # Add one lap to this team here + compute its avg speed and position
                    # Then return to the view
                    return {
                        'racing_mode': 'team',
                        'team_passed_id': team.id,
                        'team_passed_number': team.team_number,
                        'team_passed_name': team.name,
                        'team_passed_lap_count': team.lap_count}

