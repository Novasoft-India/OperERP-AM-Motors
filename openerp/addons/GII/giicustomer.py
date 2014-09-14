from osv import osv
from osv import fields

class giicustomer(osv.osv):

    _inherit="res.partner"
 
    _columns = {
            'gii_trainee':fields.one2many('trainee','gii_customerid','Trainee')
                        
            
            
        }
giicustomer()


