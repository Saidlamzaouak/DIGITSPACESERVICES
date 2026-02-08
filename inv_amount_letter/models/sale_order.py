# -*- coding: utf-8 -*-

from .amount_to_text_fr import amount_to_text_fr
from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('amount_total')
    def _compute_amount_letter(self):
        for record in self:
            record.amount_letter = amount_to_text_fr(record.amount_total, record.currency_id.symbol)

    amount_letter = fields.Text(
        string='Montant en lettres',
        compute='_compute_amount_letter',
        store=True,
        readonly=True
    )
