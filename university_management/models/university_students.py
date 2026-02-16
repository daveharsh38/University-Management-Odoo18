from odoo import api, fields, models
from odoo.exceptions import ValidationError

class UniversityStudents(models.Model):
    _name = 'university.students'
    _description = "Students Information"

    name = fields.Char("Student Name", required=True)
    roll_number = fields.Char("Roll Number")
    admission_number = fields.Char("Admission Number")
    batch = fields.Many2one("university.batch",required=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")

    teacher_id = fields.Many2one(
        'university.teachers',
        string="Class Teacher",
        ondelete='set null'
    )

    fees_state = fields.Selection([
        ('due','due'),
        ('paid','Paid'),
        ('received','Received')
        ],string="Fee status", default='due')
    fee_amount = fields.Integer(string="Your Fees",default = 39000)

    date_of_birth = fields.Date("Date of Birth")
    image = fields.Binary("Student Image")
    phone_no = fields.Char("Phone Number")
    email = fields.Char("Email")
    address = fields.Text("Address")
    user_id = fields.Many2one('res.users', string="Related User", ondelete='set null')
    active = fields.Boolean("Active", default=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)

        for rec in records:
            if not rec.batch:
                raise ValidationError("Division is required to generate Roll Number.")

            rec.admission_number = self.env['ir.sequence'].next_by_code('university.students.admission')

            seq_code = f"university.students.roll.{rec.batch.name}"
            rec.roll_number = self.env['ir.sequence'].next_by_code(seq_code)

        return records

    def fee_payment_proces(self):
        return {'type': 'ir.actions.act_window',
                'name': ('Fees Payment Portal'),
                'res_model': 'university.fees.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',}

    def open_university_portal(self):
        
        return {
            'type': 'ir.actions.act_url',
            'url': '/portal',
            'target': 'self',
        }

    def accept_payment(self):
        self.fees_state = 'received'
        return 
