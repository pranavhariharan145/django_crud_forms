# Django CRUD Manager with ModelForms, Custom Validation & File Uploads

A full-stack **Project Manager** web application built with **Django** and **Bootstrap 5**. This repository demonstrates how to build complete Create, Read, Update, and Delete (CRUD) functionality from scratch using Django's `ModelForm`, multi-layered custom form validation, file uploads (`FileField`), flash notifications, and safe record deletion.

---

## Features

- **Full CRUD Lifecycle:** Create, list, edit, and delete project records through dedicated views and Bootstrap templates.
- **ModelForm Integration:** Automatically maps model fields to styled HTML inputs (`TextInput`, `Textarea`, `NumberInput`, `ClearableFileInput`).
- **Field-Level & Cross-Field Validation:**
  - Rejects budgets less than or equal to `$0`.
  - Restricts file uploads to **5 MB max** and allowed extensions (`.pdf`, `.docx`, `.png`, `.jpg`, `.jpeg`).
  - Enforces a cross-field rule requiring at least **20 characters** in the description whenever a project budget exceeds **$10,000**.
- **PDF & Document Handling:** Saves uploaded files to `media/proposals/`, serves them directly in the browser, and cleans up files from disk upon project deletion.
- **User Feedback:** Uses Django's `messages` framework to show dismissible confirmation alerts after every action.

---

## Tech Stack

- **Backend:** Python 3.13, Django
- **Frontend:** HTML5, Bootstrap 5.3
- **Database:** SQLite3

---

## Project Structure

```text
django_crud_forms/
├── config/
│   ├── settings.py          # App registration, MEDIA_URL & MEDIA_ROOT config
│   └── urls.py              # Root routing + development media file serving
├── projects/
│   ├── templates/
│   │   └── projects/
│   │       ├── base.html                    # Shared navbar & Bootstrap alert container
│   │       ├── project_list.html            # Read view (dashboard table)
│   │       ├── project_form.html            # Create & Update view (multipart form)
│   │       └── project_confirm_delete.html  # Delete confirmation prompt
│   ├── forms.py             # ProjectForm with clean_<field>() and clean() rules
│   ├── models.py            # Project model with FileField(upload_to='proposals/')
│   ├── urls.py              # App-level URL patterns
│   └── views.py             # Function-based CRUD views
├── proposals/               # Uploaded media storage directory
├── screenshots/             # Documentation screenshots
├── db.sqlite3               # SQLite database
└── manage.py

```
---
## Screenshots

1. **Empty Dashboard** — Initial home screen showing no projects yet.
   ![Empty Dashboard](screenshots/01.png)

2. **Create Project Form** — Blank `ModelForm` page at `/create/` for adding a new project.
   ![Create Project Form](screenshots/02.png)

3. **Custom Validation Errors** — Triggers inline errors when budget exceeds $10,000 with a short description or when a file is missing.
   ![Custom Validation Errors](screenshots/03.png)

4. **Filled Create Form** — Valid project details entered along with an attached `.pdf` proposal file.
   ![Filled Create Form](screenshots/04.png)

5. **Project Created** — Redirects to the home dashboard with a success message and download link.
   ![Project Created](screenshots/05.png)

6. **PDF File Preview** — Clicking the download button opens the uploaded PDF directly in the browser.
   ![PDF File Preview](screenshots/06.png)

7. **Delete Confirmation** — Confirmation prompt at `/<id>/delete/` before removing a project.
   ![Delete Confirmation](screenshots/07.png)

8. **Project Deleted** — Redirects back to the dashboard with a deletion confirmation alert and cleans up the file.
   ![Project Deleted](screenshots/08.png)

## How to Run

```bash
pip install django
python manage.py migrate
python manage.py runserver