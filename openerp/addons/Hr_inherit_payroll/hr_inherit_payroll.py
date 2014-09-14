from osv import osv
from osv import fields

class Hr_contract(osv.osv):
    _inherit = 'hr.contract'
    
    _columns = {
                
            'x_gp':fields.float('Gross Pay',size=8, required=False, readonly=False),
            'x_festadvance':fields.float('Fest Advance',size=8, required=False, readonly=False),
            'x_pfamount':fields.float('PF Amount(Rs)',size=8, required=False, readonly=False),
            'x_pfpercentage':fields.float('PF Percentage(%)',size=8, required=False, readonly=False),
            'x_incometax':fields.float('Income Tax',size=8, required=False, readonly=False),
            
        }
    


Hr_contract()

class Hr_payslip(osv.osv):
    _inherit = 'hr.payslip'
    
    _columns = {
                
            'x_days':fields.float('Days',size=8, required=False, readonly=False),
            'x_protax':fields.float('Pro Tax',size=8, required=False, readonly=False),
            'x_pfloan':fields.float('PF Loan',size=8, required=False, readonly=False),
       
            
        }
    


Hr_payslip()

class Hr_employee(osv.osv):
    _inherit = 'hr.employee'
    
    _columns = {
                
            'x_code':fields.integer('Employee-Machine Code',size=8, required=False, readonly=False),
         
       
            
        }
    


Hr_employee()

