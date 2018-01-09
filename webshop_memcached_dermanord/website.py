# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution, third party addon
# Copyright (C) 2018- Vertel AB (<http://vertel.se>).
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
from openerp.addons.web.http import request
from openerp.addons.website_memcached import memcached

from openerp.addons.webshop_dermanord.webshop_dermanord import WebsiteSale

import logging
_logger = logging.getLogger(__name__)

class WebsiteSale(WebsiteSale):

    # '/dn_shop'
    @memcached.route()
    def dn_shop(self, page=0, category=None, search='', **post):
        return super(WebsiteSale, self).dn_shop(page, category, search, **post)

    # '/dn_list'
    @memcached.route()
    def dn_list(self, page=0, category=None, search='', **post):
        return super(WebsiteSale, self).dn_list(page, category, search, **post)

    # '/shop/product/<model("product.template"):product>'
    @memcached.route()
    def product(self, product, category='', search='', **kwargs):
        return super(WebsiteSale, self).product(product, category, search, **post)

    # '/shop/product/comment/<int:product_template_id>'
    @memcached.route()
    def product_comment(self, product_template_id, **post):
        return super(WebsiteSale, self).product_comment(product_template_id, **post)

    # '/dn_shop/variant/<model("product.product"):variant>'
    @memcached.route()
    def dn_product_variant(self, variant, category='', search='', **kwargs):
        return super(WebsiteSale, self).dn_product_variant(variant, category, search, **kwargs)

    # '/shop/cart'
    @memcached.route()
    def cart(self, **post):
        return super(WebsiteSale, self).cart(**post)

    # '/shop/cart/update'
    @memcached.route()
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        return super(WebsiteSale, self).cart_update(product_id, add_qty, set_qty, **kw)