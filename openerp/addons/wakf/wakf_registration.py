from openerp.osv import osv
from openerp.osv import fields
from openerp import tools

class wakf_registration(osv.osv):
    """
         Open ERP Model
    """
    _name = 'wakf.registration'
    _description = 'wakf.registration'
    
    
    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image, avoid_resize_medium=True)
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
    
    def on_change_wakf_village_to_taluk(self, cr, uid, ids, village_id, context=None):
        values = {}
        if village_id:
            cust = self.pool.get('wakf.village').browse(cr, uid, village_id, context=context).taluk_id.id
            cust1 = self.pool.get('wakf.village').browse(cr, uid, village_id, context=context).district_id.id
            values = {
                'taluk_id': cust,
                'district_id': cust1
            }
        return {'value' : values}
    
    
    
 
    _columns = {
            'name':fields.char('Wakf Name', size=128, required=False),
            'postoffice':fields.char('Post Office', size=128, required=False),
            'rule_succession':fields.char('Rule of Succession', size=128, required=False),
            'phone':fields.char('Phone Number', size=64, required=False),
            'wakf_old_name':fields.char('Wakf old name', size=128, required=False),
            'suomoto':fields.boolean('Suomoto',required=False),
            'type_id':fields.many2one('wakf.type','Wakf Type',ondelete='set null',required=False),
            #'wakf_reg_no':fields.many2one('wakf.id','Wakf Reg no:',ondelete='set null',required=True),
            'classification':fields.selection((('sunni','Sunni'), ('shia','Shia')),'Classification',required=False),
            'wakf_objectives':fields.text('Remarks',required=False),
            'wakf_reg_no':fields.char('Registration No',size=8,required=False),
            'wakf_registration_date':fields.date('Registration Date',required=False),
            'creation_date':fields.date('Wakf Creation Date',required=False),
            'gazetted':fields.boolean('Gazetted'),
            'gazetted_date':fields.date('Gazetted Date',required=False),
            'comm_addr':fields.text('Communication address',help='Address for communication of wakf',required=False),
            'waquif_name':fields.char('Waquif Name',size=128,required=False),
            'waquif_uid':fields.char('Waquif UID',size=32,required=False,help='Unique Identification to be assigned from the Aadhar Project'),
            'waquif_father_name':fields.char("Father/Husband's Name",size=128,required=False),
            'waquif_father_uid':fields.char("Father/Husband's UID",size=32,required=False,help='Unique Identification to be assigned from the Aadhar Project'),
            'waquif_address':fields.text('Waquif Address',required=False),
            'district_id':fields.many2one('wakf.district','District',ondelete='set null'),
            'taluk_id':fields.many2one('wakf.taluk','Taluk',ondelete='set null'),
            'village_id':fields.many2one('wakf.village','Village',ondelete='set null'), 
            'wakf_immovable_property_id':fields.one2many('wakf.immovableproperty','wakf_id','Immovable Properties'),
            'wakf_movable_property_id':fields.one2many('wakf.movableproperty','wakf_id','Movable Properties'),
            'wakf_management_id':fields.one2many('wakf.management','wakf_id','Management Details'),
            'company_id': fields.many2one('res.company', 'Company', required=True),
             # image: all image fields are base64 encoded and PIL-supported
             'waqufi_photo': fields.binary("Photo",
             help="This field holds the image used as image for the Waqfi, limited to 1024x1024px."),
            'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized image", type="binary", multi="_get_image",
            store={
                'product.product': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized image of the Waqfi. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved, "\
                 "only when the image exceeds one of those sizes. Use this field in form views or some kanban views."),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized image", type="binary", multi="_get_image",
            store={
                'wakf.registration': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized image of the Waqfi. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required.")
        }
    
    _defaults = {
        'company_id': lambda s, cr, uid, c: s.pool.get('res.company')._company_default_get(cr, uid, 'wakf.registration', context=c),
    }
    _sql_constraints = [
        ('wakf_reg_uniq', 'unique(wakf_reg_no)', 'Register Number already exists !'),
    ]
    
    
    
   
    
wakf_registration()


