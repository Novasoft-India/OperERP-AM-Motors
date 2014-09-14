from osv import osv
from osv import fields

class awardingbody(osv.osv):
 
    _name = 'test'
    _description = 'test'

    
    _columns = {
            'name':fields.char('Name', size=64, required=False, readonly=False),
            'gii_awardbodycode':fields.char('Awarding Body Code', size=64, required=False, readonly=False),
            'gii_supplierref':fields.char('Supplier Reference', size=64, required=False, readonly=False) 
        }
awardingbody()

class grading(osv.osv):

    _name = 'gii.grading'
    _description = 'gii.grading'
 
    _columns = {
            'name':fields.char('Course Id', size=64, required=False, readonly=False),
            'gii.grades':fields.char('Grade', size=64, required=False, readonly=False),
            'gii.op':fields.char('Operator', size=64, required=False, readonly=False),                        
            'gii.from':fields.char('From', size=64, required=False, readonly=False),
            'gii.to':fields.char('To', size=64, required=False, readonly=False),
            'gii.symbol':fields.char('Symbol', size=64, required=False, readonly=False),
            'gii_awardcompleted': fields.selection([('yes', 'Y'),('no','N')],'Award Completed'),            
            'product_id':fields.many2one('product.product', 'Sale Order', ondelete='set null',select=True)
        }
grading()

class language(osv.osv):
 
    _name = 'gii.language'
    _description = 'gii.language'
 
    _columns = {
            'name':fields.char('Language', size=64, required=False, readonly=False),
        }
language()

class giiqualification(osv.osv):
 
    _name = 'gii.qualification'
    _description = 'gii.qualification'
 
    _columns = {
            'gii_category_id':fields.many2one('product.category','Category',required=False,ondelete='set null'),
            'gii_awarding_id':fields.many2one('test','Awarding Body',required=False,ondelete='set null'),            
            'name':fields.char('Title', size=64, required=False, readonly=False),
            'gii_qualificationcode':fields.char('Qualification Code', size=64, required=False, readonly=False),
            'gii_qualidescript':fields.char('Qualification Description', size=64, required=False, readonly=False),
            'gii_complerequired':fields.char('Completion Requirements', size=64, required=False, readonly=False),
            'gii_designationaward':fields.char('Designation Award', size=64, required=False, readonly=False),
            'gii_qflevel_id':fields.char('QF Level', size=64, required=False, readonly=False),
            'gii_prerequisitest':fields.char('Pre-requisites', size=64, required=False, readonly=False),
            'gii_units_id': fields.selection([('single', 'Single'),('multi','Multi')],'Units'),
            'gii_bundledprice':fields.char('Bundled Price', size=64, required=False, readonly=False)
        }
giiqualification()

class duration(osv.osv):

    _name = 'gii.duration'
    _description = 'gii.duration'
 
    _columns = {
            'name':fields.char('Duration', size=64, required=False, readonly=False)
        }
duration()

class testproduct(osv.osv):

    _name = 'gii.product'
    _description = 'gii.product'
 
    _columns = {
            'name':fields.char('data', size=64, required=False, readonly=False)
        }
testproduct()

class service(osv.osv):

    _name = 'service'
    _description = 'service'
 
    _columns = {
            'name':fields.char('Service Type', size=64, required=False, readonly=False),
            'amount':fields.float('Amount', size=64, required=False, readonly=False),
            'location':fields.char('Location', size=64, required=False, readonly=False)
        }
service()

class target(osv.osv):
 
    _name = 'gii.target'
    _description = 'gii.target'
 
    _columns = {
            'name':fields.char('Target Audience', size=64, required=False, readonly=False)    
        }
target()

class assessmentcourse(osv.osv):

    _name = 'gii.assessment'
    _description = 'gii.assessment'
 
    _columns = {
            'name':fields.char('Assesment Type', size=64, required=False, readonly=False)
        }
assessmentcourse()

class giicurrency(osv.osv):

    _name = 'gii.currency'
    _description = 'gii.currency'
 
    _columns = {
            'name':fields.char('data', size=64, required=False, readonly=False)
        }
giicurrency()





class giiidtype(osv.osv):

    _name = 'idtype'
    _description = 'idtype'
 
    _columns = {
            'name':fields.char('ID Type', size=64, required=False, readonly=False)
        }
giiidtype()

class giilevels(osv.osv):
 
    _name = 'levels'
    _description = 'levels'
 
    _columns = {
          'name':fields.char('Levels', size=64, required=False, readonly=False)
        }
giilevels()


class giicategory(osv.osv):

    _name = 'category'
    _description = 'category'
 
    _columns = {
            'gii_category_id':fields.many2one('product.category','Category', ondelete='set null'),
        }
giicategory()


class giifrequency(osv.osv):

    _name = 'frequency'
    _description = 'frequency'
 
    _columns = {
            'name':fields.char('Frequency', size=64, required=False, readonly=False)
        }
giifrequency()


class giitime(osv.osv):

    _name = 'time'
    _description = 'time'
 
    _columns = {
            'name':fields.char('Time', size=64, required=False, readonly=False)
        }
giitime()

class giicity(osv.osv):

    _name = 'city'
    _description = 'city'
 
    _columns = {
             'name':fields.char('City', size=64, required=False, readonly=False),
             'city_code':fields.char('City Code', size=64, required=False, readonly=False)
        }
giicity()