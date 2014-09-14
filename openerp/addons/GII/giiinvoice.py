from osv import osv
from osv import fields

class account_invoice_line(osv.osv):
    _inherit = "account.invoice.line"
    _columns = {
           'name':fields.char('Item', size=64, required=False, readonly=False)
            }
account_invoice_line()