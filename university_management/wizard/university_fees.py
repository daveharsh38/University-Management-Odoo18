from odoo import models, fields,api


class TimeTableWizard(models.TransientModel):
    _name = "university.fees.wizard"
    _description = "Student Fees wizard"

    fee_amount = fields.Integer(string="Your Fees")
    student_id = fields.Many2one('university.students')

    def confirm_fee_payment(self):
        self.student_id.fees_state = 'paid'
        return

    def cancel_fee_payment(self):
        self.student_id.fees_state = 'due'
        return

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)        
        active_id = self.env.context.get('active_id')
        
        if active_id:
            student_id = self.env['university.students'].browse(active_id)
            
            res.update({
                'student_id': active_id,
                'fee_amount': student_id.fee_amount
            })
        return res