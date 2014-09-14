from openerp.osv import osv
from openerp.osv import fields

class wakf_management(osv.osv):
    """
         Open ERP Model
    """
    _name = 'wakf.management'
    _description = 'wakf.management'
    
    def on_change_wakf(self, cr, uid, ids, wakf_reg_no, context=None):
        values = {}
        if wakf_reg_no:
            cust = self.pool.get('wakf.registration').browse(cr, uid, wakf_reg_no, context=context)
            values = {
                'wakf_reg_no': cust.wakf_reg_no
            }
        return {'value' : values}
    def _get_active_id(self, cr, uid, ids, context=None):
        if context is None: context = {}
        return context.get('active_id', False)
 
    _columns = {
            'wakf_id':fields.many2one('wakf.registration','Wakf Name',ondelete='set null'),
            'wakf_reg_no':fields.char('Reg No:',ondelete='set null'),             
            'name':fields.char('Name', size=128, required=True),
            'name_waquif':fields.char('Waquif Name', size=128, required=False),
            'details_waquif':fields.text('Waquif Details',required=False),
            'management_id':fields.many2one('wakf.managedby','Property Managed By',ondelete='set null'),
            'from_date':fields.date('From Date',required=False),
            'to_date':fields.date('To Date',required=False),
            'name_sec':fields.char('Secretary Name', size=64, required=False),
            'addr_sec':fields.text('Secretary Address', size=128, required=False),
            'name_presi':fields.char('President Name', size=64, required=False),
            'addr_presi':fields.text('President Address', size=128, required=False),
            'managedby_address':fields.text('Muthavally Address',required=False),
            'district_id':fields.many2one('wakf.district','District',ondelete='set null'),
            'taluk_id':fields.many2one('wakf.taluk','Taluk',ondelete='set null'),
            'village_id':fields.many2one('wakf.village','Village',ondelete='set null'),
            
        }
    _defaults = {
    'name': _get_active_id,
}
wakf_management()

class wakf_managedby(osv.osv):
    
    _name = 'wakf.managedby'
    _description = 'wakf.managedby'
 
    _columns = {
                'name':fields.char('Name', size=64, required=True),
                'description':fields.text('Description',required=False),
                }
    
    
wakf_managedby()