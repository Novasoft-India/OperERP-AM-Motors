from osv import osv
from osv import fields

class am_sale(osv.osv):
    """
         Sale order customization for Adding Branch, Sales Executive and 
 
     """
    _name = 'sale.order'
    _description = 'sale.order'
    _inherit='sale.order'
    
    
    
 
    

    def check_Chasisno(self,cr,uid,ids,chase_no,context=None):  
        res = self.pool.get('sale.order').browse(cr,uid,ids,context=context)
        if res:
            for s in res:
                cha = cha + "|" + s.chase_no
            #print s.chase_no
            #if str(chase_no) == s.chase_no :      
                #res['warning']={'title':'warning','message':'Duplicate Chase Number'}  
                
        else:
            cha='Not Fetched'          
        #return res
        return { 'value' : {'client_order_ref':cha}}
    
    
    
 
    _columns = {
            'customer_demand_id':fields.one2many('ammotors.customerdemand','saleorder_id','Customer Demand'),
            'chase_no':fields.char('Chassis No',size=64,required=True),
            'deliver_branch_id':fields.many2one('ammotors.branch','Delivery Branch', ondelete='set null'),
            'delivery_date':fields.datetime('Delivery Date',required=False),
            'registration_mode':fields.selection((('t','Temporary'), ('p','Permanent'), ('u','Not-Confirmed')),'Registration Mode' ),
            'vechile_model_id':fields.many2one('ammotors.vechilemodel','Vechile Model', ondelete='set null'),
            'color_id':fields.many2one('ammotors.color','Colour', ondelete='set null'), 
            'executive_id':fields.many2one('hr.employee','Executive',domain="[('branch_id','=',deliver_branch_id)]" ,ondelete='set null')         
            
        }
    
    _sql_constraints = [
        ('chase_uniq', 'unique(chase_no)', 'Chase Number must be unique per Sales Order!'),
    ]
    
    
am_sale()


class customer_demand(osv.osv):
    
    _name='ammotors.customerdemand'
    _description='Model for storing Customer Demand'
    
    
    _columns={
              
              'item':fields.char('Item',size=64,required=False),
              'description':fields.char('Description',size=64,required=False),
              'pay':fields.selection((('p','Pay'), ('f','FOC')),'Payment Mode',required=True),
              'saleorder_id':fields.many2one('sale.order', 'Sale Order', ondelete='set null',select=True)
            
              
              
              }
customer_demand()

class vechile_model(osv.osv):
    _name='ammotors.vechilemodel'
    _description='Vechile Model Masters'
    
    
    _columns={
              'name':fields.char('Model',size=64,required=True),
              'description':fields.text('Description',required=False)
                       
              }

vechile_model()
    
    
    
class color(osv.osv):
        _name='ammotors.color'
        _description='Vechile Color Details'
        
        
        _columns={
                  'name':fields.char('Color',size=64,required=True)
                  }
        
color()
