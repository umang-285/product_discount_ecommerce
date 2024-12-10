from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _onchange_product_id_set_discounted_price(self):
        if self.product_id.discount_percentage > 0:
            self.price_unit = self.product_id.discounted_price
        else:
            self.price_unit = self.product_id.list_price
