# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_services = fields.Text(
        string='Services de la société',
        help='Liste des services offerts par la société (une ligne par service, séparés par des tirets)',
        default='ENSEIGNES - IMPRIMERIE\nMARKETING DIGITAL'
    )

    ice = fields.Char(string='Ice', required=False)
    identifiant_tp = fields.Char(string='TP', required=False)
    cnss = fields.Char(string='CNSS', required=False)

    @api.model
    def get_company_services_for_report(self, company=None, o=None):
        """Helper method to get company services for report templates"""
        company_obj = company
        if company and hasattr(company, 'company_id') and company.company_id:
            company_obj = company.company_id
        elif not company:
            if o and hasattr(o, 'company_id') and o.company_id:
                company_obj = o.company_id
            else:
                company_obj = self.env.company
        
        if company_obj and hasattr(company_obj, 'company_services') and company_obj.company_services:
            return [s.strip() for s in company_obj.company_services.split('\n') if s.strip()]
        return []


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    def get_company_with_services(self):
        """Helper method to get the actual res.company object with services"""
        self.ensure_one()
        if hasattr(self, 'company_id') and self.company_id:
            return self.company_id
        return self.env.company
    
    def get_company_services(self):
        """Get company services as a list"""
        company = self.get_company_with_services()
        if company and company.company_services:
            return [s.strip() for s in company.company_services.split('\n') if s.strip()]
        return []


class PartnerInherit(models.Model):
    _inherit = 'res.partner'


    ice = fields.Char(string='Ice', required=False)
    identifiant_tp = fields.Char(string='TP', required=False)
    cnss = fields.Char(string='CNSS', required=False)