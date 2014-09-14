from osv import osv
from osv import fields

class deliverable(osv.osv):
 
    _name = 'deliverables'
    _description = 'deliverables'
 
    _columns = {
            'name':fields.char('Course Id', size=64, required=False, readonly=False),
            'gii_location':fields.char('Location', size=64, required=False, readonly=False),
            'gii_minpers':fields.char('Minimum Persons', size=64, required=False, readonly=False),
            'gii_maxpers':fields.char('Maximum Persons', size=64, required=False, readonly=False),
            'gii_feepp':fields.char('Fee.p.p', size=64, required=False, readonly=False),
            'gii_group_disc':fields.char('Group Discount', size=64, required=False, readonly=False),
            'gii_copmpleted':fields.char('Completed', size=64, required=False, readonly=False),
            'gii_eventid':fields.char('Event Id', size=64, required=False, readonly=False)
        }
deliverable()

class giicohorts(osv.osv):
 
    _name = 'cohorts'
    _description = 'cohorts'
 
    _columns = {
            'customer_id':fields.many2one('res.partner','Cohorts', ondelete='set null') 
                  
        }
    
giicohorts()

class events(osv.osv):
 
    _name = 'event'
    _description = 'event'
 
    _columns = {
            'event_id':fields.many2one('event.event','Events', ondelete='set null')
        }
events()