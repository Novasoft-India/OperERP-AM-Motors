from openerp import tools
from openerp.osv import fields, osv

class am_bill_register_report(osv.osv):
    """
         Open ERP Model for Coir Board Commission Calculation
    """
    _name = 'am.bill.register.report'
    _description = 'am.bill.register.report'
    _auto = False
 
    _columns = {
            'number':fields.char('Invoice',size=64,readonly=True),
            'state':fields.char('State',size=64,readonly=True),
            'date_invoice': fields.date('Invoice Date', readonly=True),
            'vechile_model_id':fields.many2one('ammotors.vechilemodel','Model',readonly=True),
            'executive_id':fields.many2one('hr.employee','Executive',readonly=True),
            'deliver_branch_id':fields.many2one('ammotors.branch','Branch',readonly=True),
            'chase_no':fields.char('Chasis No',size=64,readonly=True),
            'delivery_date': fields.date('Delivery Date', readonly=True),
            'amount_untaxed': fields.float('Untaxed Amount', readonly=True),            
            'base' : fields.float('Taxable Amount',readonly=True),
            'name':fields.char('Tax Code',size=64,readonly=True),
            'amount_tax' : fields.float('Tax Amount',readonly=True),
            'amount_total' : fields.float('Bill Amount',readonly=True)
            }
    _order = 'number'
    
    
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'am_bill_register_report')
        cr.execute("""          
                CREATE OR REPLACE VIEW am_bill_register_report AS( 
                SELECT 
                    min(a_i.id) as id,
                    a_i.create_date, 
                    a_i.number, 
                    a_i.amount_tax, 
                    a_i.state, 
                    a_i.date_invoice, 
                    a_i.amount_untaxed, 
                    a_i.amount_total, 
                    a_i_t.tax_amount, 
                    a_i_t.amount, 
                    a_i_t.base, 
                    s_o.vechile_model_id, 
                    s_o.deliver_branch_id, 
                    s_o.chase_no, 
                    s_o.executive_id, 
                    s_o.delivery_date, 
                    a_i_t.name
                FROM 
                    account_invoice a_i
                    full outer join account_invoice_tax a_i_t on (a_i.id= a_i_t.invoice_id)
                    left join sale_order s_o on (s_o.id=a_i.x_so) 
                Group By
                    a_i.create_date, 
                    a_i.number, 
                    a_i.amount_tax, 
                    a_i.state, 
                    a_i.date_invoice, 
                    a_i.amount_untaxed, 
                    a_i.amount_total, 
                    a_i_t.tax_amount, 
                    a_i_t.amount, 
                    a_i_t.base, 
                    s_o.vechile_model_id, 
                    s_o.deliver_branch_id, 
                    s_o.chase_no, 
                    s_o.executive_id, 
                    s_o.delivery_date, 
                    a_i_t.name                   
                    )
                    """)
    
am_bill_register_report()
