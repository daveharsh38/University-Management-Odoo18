from odoo import api, fields, models
from odoo.exceptions import ValidationError

class University(models.Model):
    _name = 'university.subject'
    _description = "Subjects"

    name = fields.Char("Subject Name", required=True)
    code = fields.Char("Subject Code",copy=False)
    description = fields.Text("Description")
    credit = fields.Integer("Credits", default=3)
    active = fields.Boolean(default=True)
    end_date = fields.Date(string="End date for calendar")
    start_date = fields.Date(string="Start date for calendar")

    teacher_ids = fields.Many2many(
        'university.teachers',
        'university_teacher_subject_rel',
        'subject_id',
        'teacher_id',
        string="Teachers"
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if not rec.code:
                rec.code = self.env['ir.sequence'].next_by_code('university.subject.code')
        return records
