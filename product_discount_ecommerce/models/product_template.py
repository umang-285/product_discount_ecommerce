from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float(string="Discount (%)", default=0.0)

    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        for product in self:
            if product.discount_percentage > 0:
                product.discounted_price = product.list_price * (1 - (product.discount_percentage / 100))
            else:
                product.discounted_price = product.list_price

    discounted_price = fields.Float(
        string="Discounted Price",
        compute="_compute_discounted_price",
        store=True,
    )
