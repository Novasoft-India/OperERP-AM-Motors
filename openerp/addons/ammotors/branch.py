from osv import osv
from osv import fields

class branch(osv.osv):
    """
    Model for adding new Model for Storing Branch Information
    
    """
 
    _name = 'ammotors.branch'
    _description = 'ammotors.branch'
 
    _columns = {
            'name':fields.char('Name', size=64, required=True),
            'address':fields.text('Address', size=64, required=False),
            'latitude':fields.float('Latitude',required=False),
            'longitude':fields.float('Longitude',required=False),
            'employees':fields.one2many('hr.employee','branch_id','Employees'),         
            
        }
branch()