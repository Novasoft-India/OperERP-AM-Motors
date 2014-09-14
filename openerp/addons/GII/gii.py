from osv import osv
from osv import fields

class inherits(osv.osv): 
    _name = 'product.product'
    _description = 'product.product'
    _inherit="product.product"
 
    _columns = {
                'gii_cc':fields.char('Course Code', size=64, required=False, readonly=False),
                'gii_ver':fields.char('Version', size=64, required=False, readonly=False),
                'gii_effect':fields.date('Effective Date', size=64, required=False, readonly=False),
                'gii_with':fields.date('Withdrawn Date', size=64, required=False, readonly=False),
                'gii_with':fields.date('Withdrawn Date', size=64, required=False, readonly=False),
                'gii_language':fields.many2one('gii.language','Language', ondelete='set null'),
         'gii_reccomended_study':fields.integer('Recommended Study Hours', size=64, required=False, readonly=False),
         'gii_minimum_attendance':fields.integer('Min Attendance Rate Required', size=64, required=False, readonly=False),      
         'gii_glh':fields.integer('GLH', size=64, required=False, readonly=False), 
         'gii_qf_id':fields.many2one('gii.qflevel','QF Level', ondelete='set null'),                            
         'gii_name':fields.text('Reccomended for', size=64, required=False, readonly=False), 
         'gii_lo':fields.text('Learning Objectives', size=64, required=False, readonly=False),       
         'gii_credit_id':fields.one2many('gii.accreditations','product_id','Accreditations'),
         'gii_grading_id':fields.one2many('gii.grading','product_id','Grading'),
         'gii_events_id':fields.one2many('event.event','productid_event','Events'),
         'gii_fees_id':fields.one2many('gii.fee','product_id','Fees'),
         'gii_resources_id':fields.one2many('gii.resources','product_id','Resources'),
         'gii_coursetutors_id':fields.one2many('gii.coursetutors','product_id','Course Tutors'),
         'gii_assmnt_id':fields.many2one('gii.assessment','Assesment Type', ondelete='set null'),
         'gii_target_id':fields.many2one('gii.target','Target Audience', ondelete='set null'),
         'gii_awardingbody_id':fields.many2one('test','Awarding Body',required=True, ondelete='set null'),
         'gii_qualification_id':fields.many2one('gii.qualification','Qualification',required=True, ondelete='set null')                    
             }
inherits()



class accreditations(osv.osv):

    _name = 'gii.accreditations'
    _description = 'gii.accreditations'
 
    _columns = {
            'name':fields.char('Accrediting Body', size=64, required=False, readonly=False),
            'gii_accfrom':fields.date('Accreditation From', size=64, required=False, readonly=False),
            'gii_accto':fields.date('Accreditation to', size=64, required=False, readonly=False),
            'gii_qua':fields.char('Qualification', size=64, required=False, readonly=False),
            'gii_level':fields.char('Credits Level', size=64, required=False, readonly=False),
            'gii_amt':fields.integer('Credits Amount', size=64, required=False, readonly=False),
            'gii_pmr':fields.char('Pass Mark Required', size=64, required=False, readonly=False),            
            'gii_cur':fields.many2one('res.currency','Currency',required=False,ondelete='set null'),
            'gii_fee':fields.integer('Fee', size=64, required=False, readonly=False),
            'gii_submissiondate':fields.date('Submission Date', size=64, required=False, readonly=False),
            'gii_accreremarks':fields.text('Remarks', size=64, required=False, readonly=False),
            'product_id':fields.many2one('product.product', 'Sale Order', ondelete='set null',select=True)
        }
accreditations()


class coursetutors(osv.osv):
 
    _name = 'gii.coursetutors'
    _description = 'gii.coursetutors'
 
    _columns = {
           'name':fields.char('Course Id', size=64, required=False, readonly=False),
           'gii_tutor_employee':fields.char('Employee Id', size=64, required=False, readonly=False),
           'gii_tutor':fields.many2one('hr.employee','Tutor',required=False,ondelete='set null'),
           'product_id':fields.many2one('product.product', 'Sale Order', ondelete='set null',select=True)
        }
coursetutors()



class fees(osv.osv):

    _name = 'gii.fee'
    _description = 'gii.fee'
 
    _columns = {
            'name':fields.many2one('service', 'Service Type', ondelete='set null',select=True),
            'gii_eventtype':fields.many2one('event.type', 'Event Type', ondelete='set null',select=True),
            'gii_hrs':fields.float('Hours', size=64, required=False, readonly=False),
            'gii_city':fields.many2one('city', 'City', ondelete='set null',select=True),
            'gii_curr':fields.many2one('res.currency','Currency',required=False,ondelete='set null'),
            'gii_feee':fields.float('Fee', size=64, required=False, readonly=False),
            'gii_gd': fields.selection([('yes', 'Y'),('no','N')],'Group Discounts'),
            'gii_bd': fields.selection([('yes', 'Y'),('no','N')],'Bundling Discounts'),
            'gii_md':fields.float('Membership Discount', size=64, required=False, readonly=False),
            'gii_remarks':fields.text('Remarks', size=64, required=False, readonly=False),
            'product_id':fields.many2one('product.product', 'product', ondelete='set null',select=True)
        }
fees()


class resources(osv.osv):

    _name = 'gii.resources'
    _description = 'gii.resources'
 
    _columns = {
            'name':fields.char('Item', size=64, required=False, readonly=False),
            'gii_supplier':fields.char('Supplier', size=64, required=False, readonly=False),
            'gii_curren':fields.many2one('res.currency','Currency',required=False,ondelete='set null'),
            'gii_cost':fields.float('Cost', size=64, required=False, readonly=False),
            'gii_expense':fields.float('Expense Account', size=64, required=False, readonly=False),
            'product_id':fields.many2one('product.product', 'product', ondelete='set null',select=True)
            
        }
resources()


class qflevel(osv.osv):

    _name = 'gii.qflevel'
    _description = 'gii.qflevel'
 
    _columns = {
            
            'name':fields.char('QF Level', size=64, required=False, readonly=False)           
            
        }
qflevel()






