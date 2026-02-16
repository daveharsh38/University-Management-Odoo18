from odoo import http
from odoo.http import request

class UniversityPortal(http.Controller):
    @http.route(['/portal'], type="http", auth="public", website=True)
    def my_portal(self, **kwargs):
        # Fetching detailed statistics
        students = request.env['university.students'].search([])
        lectures = request.env['university.lecture'].search([], order="start_datetime desc", limit=5)
        
        values = {
            'student_count': len(students),
            'teacher_count': request.env['university.teachers'].search_count([]),
            'subject_count': request.env['university.subject'].search_count([]),
            'students': students,
            'upcoming_lectures': lectures,
        }
        return request.render("university_management.university_portal", values)
