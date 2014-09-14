from osv import osv
from osv import fields

class details_of_training(osv.osv):

    _name = 'detailsof.training'
    _description = 'detailsof.training'
 
    _columns = {
            'name':fields.char('Serial No', size=8, required=False, readonly=False),
            'course_name':fields.char('Name of the course of training', size=32, required=False, readonly=False),
            'institution_name':fields.char('Name of Institution', size=32, required=False, readonly=False),
            'period_from':fields.date('Period From', required=False, readonly=False),
            'period_to':fields.date('Period To', required=False, readonly=False),
            'remarks_training':fields.text('Remarks if any',size=32, required=False, readonly=False),
            'training_id':fields.many2one('hr.employee','test_trining',ondelete='set null'),
        }
details_of_training()