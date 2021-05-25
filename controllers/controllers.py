# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

import logging
_logger = logging.getLogger(__name__)

class WebsiteSaleGiftController(WebsiteSale):
	@http.route(['/shop/update_gift'], type='json', auth='public', methods=['POST'], website=True, csrf=False)
	def update_eshop(self, **post):
		results = {}
		results = self._add_website_sale_gift(**post)
		return results

	def _add_website_sale_gift(self, **post):
		order = request.website.sale_get_order()

		order.is_gift = post['gift_id']

		return {
			'status': True,
		}
