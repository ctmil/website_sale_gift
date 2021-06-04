# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WebsiteSaleGift(models.Model):
    _inherit = 'sale.order'

    is_gift = fields.Boolean('¿Es para regalo?')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_create_images(self):
        recs = self.search([])
        img = self.env['product.image'].search([('name', '=', 'final')], limit=1)

        for rec in recs:
            self.env['product.image'].create({'product_tmpl_id': rec.id, 'name': 'final', 'image': img.image})