from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class PortalDetailInformation(CustomerPortal):

    def _get_mandatory_fields(self):
        return super()._get_mandatory_fields() + ["country_code"]
    
    def details_form_validate(self, data, partner_creation=False):
        error, error_message = super().details_form_validate(data, partner_creation)

        partner = request.env.user.partner_id

        #country validation
        country_id = data.get('country_id')
        country = request.env['res.country'].sudo().search([('phone_code', '=', data.get('country_code'))]) 
        if country_id: 
            if int(country_id) != country.id:
                error['country_id'] = 'error'
                error_message.append(_('Your phone code and country did not match. (Phone Code : %s)') % country.code)

        #phone number unique
        phone = data.get('phone')
        if phone:
            existing_partner = request.env['res.partner'].sudo().search([
                ('phone', '=', phone),
                ('id', '!=', partner.id)  # compare with other people
            ], limit=1)
            if existing_partner:
                error['phone'] = 'error'
                error_message.append('The phone number has already been taken!')

        return error, error_message
