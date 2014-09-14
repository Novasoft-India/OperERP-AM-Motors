from osv import osv
from osv import fields

class hr_career(osv.osv):

    _name = 'hr.career'
    _description = 'hr.career'
 
    _columns = {
                
            'name':fields.char('Serial No',size=8, required=False, readonly=False),
            'test_attended_id':fields.many2one('test.attended','Name of examination',ondelete='set null'),
            'register_no_exam':fields.char('Register No',size=8, required=False, readonly=False),
            'year_of_passing':fields.date('Year of Passing',required=False, readonly=False),           
            'test_result':fields.char('Result', size=64, required=False, readonly=False),
            'test_name':fields.many2one('hr.employee','testname',ondelete='set null'),
            
        }
hr_career()

class test_attended(osv.osv):

    _name = 'test.attended'
    _description = 'test.attended'
 
    _columns = {
            'name':fields.char('Name of examination ', size=64, required=False, readonly=False),
            'description':fields.char('description', size=64, required=False, readonly=False),
            
            
        }
test_attended()
