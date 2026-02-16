# University Computer Science Department Management System (Odoo 18)

A professional **Odoo 18** portfolio module that demonstrates my **basic + practical understanding of Odoo development**: ORM models & relations, views (list/form), menus/actions, sequences, business logic, wizards, reports, and controllers/portal-ready structure.

> ✅ **Note:** **Access Rights / Record Rules** are planned for an upcoming update (roadmap below).  
> Current version focuses on core models, UI, workflows, and automation-ready structure.

---

## ✨ What this module demonstrates (Odoo Developer Skills)

This project is built to show I understand:

- **Odoo ORM** (models, fields, CRUD, constraints)
- **Relational fields** (Many2one, One2many, Many2many)
- **Views & UI** (form/list, notebook pages, smart buttons, statusbar states)
- **Business workflows** (state fields + buttons)
- **Wizards** using `TransientModel` (bulk actions / reporting inputs)
- **Sequences** for unique numbers (enrollment/admission/etc.)
- **Reports** (QWeb PDF report structure)
- **Controllers** (portal/web endpoints – structure included / extendable)
- **Automation-ready** design (cron hooks / scheduled actions support)
- Clean separation of concerns: **models / views / wizards / controllers / reports / security**

---

## 🧩 Functional Scope (Current)

- Manage **Students** (profile, contact info, lifecycle states)
- Manage **Teachers**
- Academic structure basics (Subjects / Batches / Division - as per implementation)
- Wizards for operations like **Fees / Timetable** (as implemented)
- Report templates (QWeb) for printable documents (if included)
- Portal/controller structure to extend (if included)

---

## 📁 Module Structure (Files Explained Simply)

Below is a simple explanation of each major file/folder type used in an Odoo module.
(Names may vary slightly depending on your module structure.)

### 1) `__manifest__.py`
- The module “identity card”.
- Defines: module name, version, dependencies, data files (views, security, reports), install flags.

### 2) `__init__.py` (root)
- Loads Python packages for Odoo.
- Typically imports `models`, `wizard`, `controllers`.

---

## 🧠 Python Layer

### `models/`
All business entities live here (database tables + business logic).

Typical files you may have:

- `models/__init__.py`  
  Imports model files so Odoo loads them.

- `models/cs_students.py` (example)
  - Defines the Student model (`_name = 'cs.students'`)
  - Uses fields like `Char`, `Date`, `Selection`, `Binary`, etc.
  - Includes constraints/validations (`@api.constrains`) and computed fields if any.
  - Handles lifecycle/workflow via `state` + buttons.

- `models/cs_teachers.py` (example)
  - Defines Teacher model (`cs.teachers`)
  - Links teachers with students/subjects using relations where required.

- `models/subjects.py` / `models/batches.py` (if present)
  - Academic master data models.

✅ **What this shows:** I can design proper models and relations and write clean Odoo business logic.

---

## 🧾 XML Views (UI Layer)

### `views/`
Defines how the data is shown inside Odoo.

Common files:

- `views/menu.xml`
  - Creates menus + submenus so the module appears in Odoo’s main UI.

- `views/students_view.xml`
  - Form/list views for students
  - Notebook pages, grouping fields, statusbar for states
  - Buttons for actions (Enroll/Graduate/etc.)

- `views/teachers_view.xml`
  - Form/list views for teachers

✅ **What this shows:** I understand actions, menus, views, and building a usable backend UI.

---

## 🧙 Wizards (Transient Models)

### `wizard/`
Wizards are temporary forms used for bulk actions or parameter-driven operations.

Typical files:

- `wizard/__init__.py`
  - Imports wizard Python files.

- `wizard/university_fees.py` (example)
  - Wizard logic (TransientModel)
  - Collects inputs (student, date range, batch, etc.)
  - Executes an action (generate fees, compute totals, print report, etc.)

- `wizard/university_fees.xml` (example)
  - Wizard form view + buttons (Confirm/Cancel)
  - Binds wizard to an action

- `wizard/time_table_wizard.py` + `.xml` (if present)
  - Helps generate/print timetable or filter schedules

✅ **What this shows:** I can build wizards properly using TransientModel + XML + actions.

---

## 🌐 Controllers (Portal / Website)

### `controllers/`
Controllers define HTTP routes (`/some/url`) for website/portal access.

Typical files:

- `controllers/__init__.py`
  - Loads controller files

- `controllers/portal.py` (example)
  - Routes for student/teacher portal pages
  - Can render templates and fetch records securely (later with access rules)

✅ **What this shows:** I understand Odoo web controllers and portal-ready architecture.

---

## 🖨️ Reports (QWeb PDF)

### `report/` or `reports/`
Contains report templates and report actions.

Typical files:

- `report/*.xml`
  - QWeb templates used for PDF printing

✅ **What this shows:** I understand printable reporting in Odoo using QWeb.

---

## 🔒 Security (Planned / Upcoming Update)

### `security/`
Usually includes:
- `ir.model.access.csv` (model access rights)
- `security.xml` (groups + record rules)

> 🚧 **Upcoming:** Access Rights / Record Rules will be added in the next update.
This will include:
- User groups (Admin / Staff / Student)
- Model access rights
- Record rules (e.g., students can only view their own record in portal)

✅ **What this will show:** understanding of security groups, access control, and multi-user permissions.

---

## ⚙️ Installation

1. Copy this module folder into your Odoo addons path:
   - Example: `custom_addons/university_management/`

2. Restart Odoo server.

3. Enable Developer Mode (optional but helpful).

4. Go to **Apps** → click **Update Apps List**.

5. Search the module name → **Install**.

---

## ✅ Usage

After installing:
- Open the module menu (example: **My School / University / CS Department**)
- Create Students & Teachers
- Use buttons to change student state (Draft → Enrolled → Graduated/Suspended)
- Use Wizards for fees/timetable operations (if available in menus/actions)
- Print reports (if report actions exist)

---

## 🛣️ Roadmap (Next Updates)

- [ ] Add full **Access Rights + Record Rules**
- [ ] Student & Teacher **Portal pages**
- [ ] Attendance module + smart buttons
- [ ] Exams & Results workflow + report card PDF
- [ ] Automated scheduled actions (cron) for reminders (fees due / upcoming exams)
- [ ] Chatter integration (`mail.thread`) for logging history on records

---

## 🧑‍💻 Author

**Harsh Mukeshkumar Dave**  
- GitHub: https://github.com/daveharsh38  
- LinkedIn: https://www.linkedin.com/in/harsh-dave-391005233/  

---

## 📜 License
This project is for learning/portfolio use. You can add a license if you want (MIT recommended).
