# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WebsiteSaleGift(models.Model):
    _inherit = 'sale.order'

    is_gift = fields.Boolean('¿Es para regalo?')