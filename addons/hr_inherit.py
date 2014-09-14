from osv import osv
from osv import fields

class hr_employee(osv.osv):
   
    _inherit="hr.employee"
    
    

    _columns = {
            
              'test_name_id':fields.one2many('hr.career','test_name'),
              'test_training':fields.one2many('hr.training','training_id'),
              'edu_qualif':fields.one2many('hr.qualification','qualification_id'),
               
              'father_name':fields.char('Name of father ',size=32,required=False),
              'hus_wife_name':fields.char('Name of Husband/Wife ',size=32,required=False),
              'religion_name':fields.char('Religion',size=16,required=False),
              'class_or_race_name':fields.char('Class or Race ',size=16,required=False),
              'community_name':fields.char('Community',size=16,required=False),
              'scheduled_cast':fields.char('Member of scheduled caste?',size=16,required=False),
              'scheduled_tribe':fields.char('Member of scheduled tribe?',size=16,required=False),
              'backward_community':fields.char('Backward community?',size=16,required=False),
                
              'sl_no':fields.char('S.l No',size=8,required=False),
              'exam_passed':fields.char('Examination Passed',size=32,required=False),
              'university':fields.char('University/Institution',size=32,required=False),
              'year_of_passing':fields.date('Year of passing',required=False),
              'register_no':fields.char('Register No',size=8,required=False),
              
              'identification_mark_1':fields.char('Personal Mark of Identification-1',size=64,required=False),
              'identification_mark_2':fields.char('Personal Mark of Identification-2',size=64,required=False), 
              
              'appointment_details':fields.char('Appointment details',size=64,required=False),
              'appoint_date':fields.date('Appointed date',required=False), 
              'superannuation_date':fields.date('date of superannuation',required=False),     
               
        }
    

hr_employee()

class details_of_training(osv.osv):

    _name = 'hr.training'
    _description = 'hr.training'
 
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




class educational_qualification(osv.osv):

    _name = 'hr.qualification'
    _description = 'hr.qualification'
 
    _columns = {
            'sl_no':fields.char('S.l No',size=8,required=False),
            'exam_passed':fields.char('Examination Passed',size=32,required=False),
            'university':fields.char('University/Institution',size=32,required=False),
            'year_of_passing':fields.date('Year of passing',required=False),
            'register_no':fields.char('Register No',size=8,required=False),
            'qualification_id':fields.many2one('hr.employee','Educational Qualifications',ondelete='set null',required=False,invisible='1'),
        }
educational_qualification()


