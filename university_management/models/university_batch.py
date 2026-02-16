from odoo import api, fields, models
from odoo.exceptions import ValidationError

class UniversityBatch(models.Model):
    _name = 'university.batch'
    _description = "Students Batch"

    name = fields.Char("Student Name", required=True)
    