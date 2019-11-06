# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2019- Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import http
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)


# ~ http://maria:8069/sv_SE/reseller/5522/consumer

class Main(http.Controller):
    @http.route(['/reseller/<int:reseller>/consumer'], type='http', auth='public', website=True)
    def add_consumer(self, reseller, **post):
        _logger.warn('\n\n\n\n\n\n\n\n FIRST NAME:')
        # ~ return http.request.render('webshop_consumer.add_consumer', {'help':{}, 'validate':{}, 'reseller':{request.env['res.partner'].sudo().browse('reseller')} })
        return http.request.render('webshop_consumer.add_consumer', {'help':{}, 'validate':{}, 'reseller':request.env['res.partner'].sudo().browse(reseller) })


    @http.route(['/reseller/<int:reseller>/insert_consumer'], type='http', auth='public', website=True)
    def insert_consumer(self, reseller, **post):
        _logger.warn('\n\n\n\n\n\n\n\n greeting!!: %s' % post.get('name', ''))

        if post.get('name') and post.get('street') and post.get('zip') and post.get('city') and post.get('country') and post.get('email'):
            ## INSERT NEW USER
            request.env['res.users'].sudo().create({
                'name': post.get('name', ''),
                'street': post.get('street', ''),
                'zip': post.get('zip', ''),
                'city': post.get('city', ''),
                'country': post.get('country', ''),
                'login': post.get('email', ''),
                'email': post.get('email', ''),
            })
            return http.request.render('webshop_consumer.insert_consumer', {'help':{}, 'validate':{}, 'reseller':request.env['res.partner'].sudo().browse(reseller) })
        else:
            ## ELSE RETURN TO PAGE FOR REGISTER
            return http.request.render('webshop_consumer.add_consumer', {'help':{}, 'validate':{}, 'reseller':request.env['res.partner'].sudo().browse(reseller) })
