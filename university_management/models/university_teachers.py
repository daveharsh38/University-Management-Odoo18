from odoo import models, fields, api

class UniversityTeachers(models.Model):
    _name = 'university.teachers'
    _description = "Teachers Information"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Teacher Name", required=True, tracking=True)
    employee_id = fields.Char("Employee ID", readonly=True, copy=False, tracking=True)

    image = fields.Binary("Photo")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")

    date_of_birth = fields.Date("Date of Birth")
    joining_date = fields.Date("Joining Date", tracking=True)

    phone = fields.Char("Phone")
    email = fields.Char("Email")
    address = fields.Text("Address")

    qualification = fields.Char("Qualification")
    experience_years = fields.Integer("Experience (Years)")

    subject_ids = fields.Many2many(
        'university.subject',
        'university_teacher_subject_rel',
        'teacher_id',
        'subject_id',
        string="Subjects Teaching"
    )

    student_ids = fields.One2many(
        'university.students',
        'teacher_id',
        string="Students"
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('on_leave', 'On Leave'),
        ('resigned', 'Resigned')
    ], default='draft', tracking=True)

    active = fields.Boolean(default=True)

    student_count = fields.Integer(compute='_compute_student_count', string="Students")

    @api.depends('student_ids')
    def _compute_student_count(self):
        for rec in self:
            rec.student_count = len(rec.student_ids)

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if not rec.employee_id:
                rec.employee_id = self.env['ir.sequence'].next_by_code('university.teachers.employee')
        return records
