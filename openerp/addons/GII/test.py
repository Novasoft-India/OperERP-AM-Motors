from osv import osv
from osv import fields

class giitrainee(osv.osv):

    _name = 'trainee'
    _description = 'trainee'
    
    def create(self, cr, uid, vals, context=None):
        if not 'gii_trainepin' in vals or vals['gii_trainepin'] == '/':
            vals['gii_trainepin'] = self.pool.get('ir.sequence').get(
                    cr, uid, 'trainee')
        return super(giitrainee, self).create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if not hasattr(ids, '__iter__'):
            ids = [ids]
        products_without_code = self.search(
                cr, uid,
                [('gii_trainepin', 'in', [False, '/']),
                 ('id', 'in', ids)],
                context=context)
        direct_write_ids = set(ids) - set(products_without_code)
        super(giitrainee, self).write(cr, uid,
                                           list(direct_write_ids),
                                           vals, context=context)
        for product_id in products_without_code:
            vals['gii_trainepin'] = self.pool.get('ir.sequence').get(
                    cr, uid, 'trainee')
            super(giitrainee, self).write(cr, uid,
                                               product_id,
                                               vals,
                                               context=context)
        return True

    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        product = self.read(cr, uid, id, ['gii_trainepin'], context=context)
        if product['gii_trainepin']:
            default.update({
                'gii_trainepin': product['gii_trainepin'] + _('-copy'),
            })

        return super(giitrainee, self).copy(cr, uid, id, default, context)
 
    _columns = {
             'name':fields.char('First Name', size=64, required=True, readonly=False),
             'gii_middlename':fields.char('Middle Name', size=64, required=False, readonly=False),
             'gii_lastname':fields.char('Last Name', size=64, required=True, readonly=False),
             'gii_address1':fields.char('Address', size=64, required=False, readonly=False),
             'gii_address2':fields.char( size=64, required=False, readonly=False),
             'gii_address3':fields.char( size=64, required=False, readonly=False),
             'gii_city':fields.char( 'City',size=64, required=False, readonly=False),
             'gii_state':fields.char( 'State',size=64, required=False, readonly=False),
             'gii_zip':fields.char('Zip', size=64, required=False, readonly=False),
             'gii_salutation_id':fields.many2one('salutation','Salutation', ondelete='set null'),
             'gii_national_id':fields.many2one('res.country','Country', ondelete='set null'),
             'gii_address': fields.selection([('yes', 'Y'),('no','N')],'Use Customer Address'),
             'gii_trainepin':fields.char('Trainee Pin', size=64, required=False, readonly=False),             
             'gii_idtype_id':fields.many2one('idtype','ID Type', ondelete='set null'),             
             'gii_phonecode':fields.char('Phone Country Code', size=64, required=False, readonly=False),
             'gii_phone':fields.char('Phone', size=64, required=False, readonly=False),
             'gii_directphone':fields.char('Direct Work Phone', size=64, required=False, readonly=False),
             'gii_mobile':fields.char('Mobile', size=64, required=False, readonly=False),
             'gii_fax':fields.char('Fax', size=64, required=False, readonly=False),
             'gii_email':fields.char('Email', size=64, required=False, readonly=False),
             'gii_secemail':fields.char('Secondary Email', size=64, required=False, readonly=False),
             'gii_gender': fields.selection([('male', 'Male'),('female','Female')],'Gender'),
             'gii_dobirth':fields.date('Date Of Birth', size=64, required=False, readonly=False),
             'gii_nationality_id':fields.many2one('res.country','Nationality', ondelete='set null'),
             'gii_lang':fields.char('Languages', size=64, required=False, readonly=False),
             'gii_areaofintrest':fields.char('Area Of Interest', size=64, required=False, readonly=False),
             'gii_suffix':fields.char('Suffix', size=64, required=False, readonly=False),
             'gii_address': fields.selection([('yes', 'Y'),('no','N')],'Use Customer Address'),
             'gii_idnumber':fields.char('ID Number', size=64, required=False, readonly=False),
             'gii_employ':fields.char('Employer', size=64, required=False, readonly=False),
             'gii_jobtitle':fields.char('Job Title', size=64, required=False, readonly=False),
             'gii_dept':fields.char('Department', size=64, required=False, readonly=False),
             'gii_membership_id':fields.many2one('levels','Level', ondelete='set null'),
             'gii_joiningdate':fields.date('GII Joining Date', size=64, required=False, readonly=False),
             'gii_expirydate':fields.date('GII Membership Expiry Date', size=64, required=False, readonly=False),
             'gii_customerid':fields.many2one('res.partner','Customer ID', ondelete='set null'),
             'gii_trainepin': fields.char('Trainee pin',
                                    size=64,
                                    select=True,
                                    required=True),
                }
    _sql_constraints = [
        ('uniq_default_code',
         'unique(default_code)',
         'The reference must be unique'),
                ]

    _defaults = {
        'gii_trainepin': '/',
        
        }    
giitrainee()
    



class giisalutation(osv.osv):
 
    _name = 'salutation'
    _description = 'salutation'
 
    _columns = {
            'name':fields.char('Salutation', size=64, required=True, readonly=False)
        }
giisalutation()

