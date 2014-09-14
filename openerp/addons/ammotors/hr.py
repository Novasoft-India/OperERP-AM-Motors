from osv import osv
from osv import fields

class hr_employee(osv.osv):
    
    _inherit="hr.employee"
    

    _columns = {
        'lastevaluation_date':fields.date('Evaluvation Date'),
        'lastincrement_date':fields.date('Last Increment Date'),
        'statutory_base':fields.float('Statutory Base',required=True),
        'leaving_reason':fields.text('Reason for Leaving',required=False),
      # 'ageing':fields.function(_ageing, type='float', obj='hr.employee', method=True, store=False, string='Ageing'),
        'branch_id':fields.many2one('ammotors.branch', 'Branch', ondelete='set null')
        
            
    }
        
hr_employee()