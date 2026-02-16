from odoo import api, fields, models
from odoo.exceptions import ValidationError


class UniversityLecture(models.Model):
    _name = "university.lecture"
    _description = "Lecture (Timetable)"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "start_datetime"

    name = fields.Char(string="Title", compute="_compute_name", store=True)

    batch_id = fields.Many2one("University.batch", required=True, tracking=True)
    subject_id = fields.Many2one("University.subject", required=True, tracking=True)
    teacher_id = fields.Many2one("University.teachers", required=True, tracking=True)

    start_datetime = fields.Datetime(required=True, tracking=True)
    end_datetime = fields.Datetime(required=True, tracking=True)

    room = fields.Char()
    note = fields.Char()

    state = fields.Selection(
        [("draft", "Draft"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled")],
        default="draft",
        tracking=True,
    )

    @api.depends("batch_id", "subject_id", "teacher_id")
    def _compute_name(self):
        for rec in self:
            parts = []
            if rec.subject_id:
                parts.append(rec.subject_id.name)
            if rec.batch_id:
                parts.append(rec.batch_id.name)
            if rec.teacher_id:
                parts.append(rec.teacher_id.name)
            rec.name = " | ".join(parts) if parts else "Lecture"

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

    def action_set_draft(self):
        self.write({"state": "draft"})

    def action_view_batch_timetable(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Batch Timetable",
            "res_model": "University.lecture",
            "view_mode": "calendar,list,form",
            "domain": [("batch_id", "=", self.batch_id.id)],
        }

    @api.constrains("start_datetime", "end_datetime")
    def _check_time(self):
        for rec in self:
            if rec.start_datetime and rec.end_datetime and rec.end_datetime <= rec.start_datetime:
                raise ValidationError("End time must be after Start time.")

    @api.constrains("teacher_id", "start_datetime", "end_datetime")
    def _check_teacher_overlap(self):
        for rec in self:
            if not rec.teacher_id or not rec.start_datetime or not rec.end_datetime:
                continue
            domain = [
                ("id", "!=", rec.id),
                ("teacher_id", "=", rec.teacher_id.id),
                ("start_datetime", "<", rec.end_datetime),
                ("end_datetime", ">", rec.start_datetime),
                ("state", "!=", "cancelled"),
            ]
            if self.search_count(domain):
                raise ValidationError("This teacher already has a lecture in this time slot.")

    @api.constrains("batch_id", "start_datetime", "end_datetime")
    def _check_batch_overlap(self):
        for rec in self:
            if not rec.batch_id or not rec.start_datetime or not rec.end_datetime:
                continue
            domain = [
                ("id", "!=", rec.id),
                ("batch_id", "=", rec.batch_id.id),
                ("start_datetime", "<", rec.end_datetime),
                ("end_datetime", ">", rec.start_datetime),
                ("state", "!=", "cancelled"),
            ]
            if self.search_count(domain):
                raise ValidationError("This batch already has a lecture in this time slot.")
