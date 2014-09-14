from osv import osv
from osv import fields

class inheritsale(osv.osv):
 
    _name = 'sale.order'
    _description = 'sale.order'
    _inherit='sale.order'
    
    _columns = {
            'name':fields.char('data', size=64, required=False, readonly=False)
        }
inheritsale()