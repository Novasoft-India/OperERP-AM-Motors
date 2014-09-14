from osv import osv
from osv import fields

class giievent(osv.osv):

    _inherit="event.event"
 
    _columns = {
            'gii_project_id':fields.many2one('project.project','Project', ondelete='set null'),
            'gii_public':fields.boolean('Public',required=False, readonly=False),
            'gii_lang':fields.many2one('gii.language','Language', ondelete='set null'),
            'gii_result_id':fields.one2many('result','product_id_event','Result'),
            'gii_session_id':fields.one2many('session','product_id_event','Session Planning'),
            'gii_sessionplanning_id':fields.one2many('sessionplanning','product_id_event','Session Planning'),
            'gii_comment':fields.text('Tutors Comment', size=64, required=False, readonly=False),
            'productid_event':fields.many2one('product.product', 'Sale Order', ondelete='set null',select=True)
            
              }
giievent()

class giiresult(osv.osv):

    _name = 'result'
    _description = 'result'
 
    _columns = {
            'name':fields.char('Reg No', size=64, required=False, readonly=False),
            'gii_customer_id':fields.many2one('res.partner','Name', ondelete='set null'),
            'gii.attendance.event':fields.char('Attendance', size=64, required=False, readonly=False),                                    
            'gii.mark.event':fields.integer('Exam Marks', size=64, required=False, readonly=False),
            'gii.grade.event': fields.selection([('p', 'P'),('m','M'),('d','D'),('f','F')],'Grade'),
            'gii.awardcompleted.event': fields.selection([('yes', 'Y'),('no','N')],'Award Completed'),
            'gii.certificate.event':fields.date('Certificate Issue Date', size=64, required=False, readonly=False),            
            'gii.remarks.event':fields.char('Remarks', size=64, required=False, readonly=False),            
            'product_id_event':fields.many2one('event.event', 'Sale Order', ondelete='set null',select=True)
            
        }
giiresult()


class giisession(osv.osv):

    _name = 'session'
    _description = 'session'
 
    _columns = {
            'name':fields.date('Session Date', size=64, required=False, readonly=False),
            'gii_timestart':fields.many2one('time','Time Starts', ondelete='set null'),
            'gii_timeend':fields.many2one('time','Time Ends', ondelete='set null'),
            'gii_tutor':fields.many2one('hr.employee','Lecturer', ondelete='set null'),
            'gii_subject':fields.char('Subject', size=64, required=False, readonly=False),
            'gii_remarks':fields.text('Remarks', size=64, required=False, readonly=False),            
            'product_id_event':fields.many2one('event.event', 'Sale Order', ondelete='set null',select=True),
            'gii_sessionlanning_id':fields.many2one('sessionplanning', 'Sale Order', ondelete='set null',select=True)
        }
giisession()

class sessionplanning(osv.osv):
 
    _name = 'sessionplanning'
    _description = 'sessionplanning'
 
    _columns = {
            'gii_holi':fields.boolean('Skip Holidays',required=False, readonly=False),            
            'gii_dur_id':fields.many2one('gii.duration','Duration (hours)', ondelete='set null'),
            'gii_freq_id':fields.many2one('frequency','Frequency', ondelete='set null'),
            'gii_starttime_id':fields.many2one('time','Session Starting Time', ondelete='set null'),
            'gii_endtime_id':fields.many2one('time','Session Ending Time', ondelete='set null'),
            'gii_breaktime_id':fields.many2one('gii.duration','Add Break Time (minutes)', ondelete='set null'),
            'gii_session_id':fields.one2many('session','product_id_event','Session Planning'),
            'gii_sun':fields.boolean('SUN',required=False, readonly=False),
            'gii_mon':fields.boolean('MON',required=False, readonly=False),
            'gii_tue':fields.boolean('TUE',required=False, readonly=False),
            'gii_wed':fields.boolean('WED',required=False, readonly=False),
            'gii_thu':fields.boolean('THU',required=False, readonly=False),
            'gii_fri':fields.boolean('FRI',required=False, readonly=False),
            'gii_sat':fields.boolean('SAT',required=False, readonly=False),
            'product_id_event':fields.many2one('event.event', 'Sale Order', ondelete='set null',select=True)
            
        }
sessionplanning()

