# Django CRUD Manager with ModelForms, Custom Validation & File Uploads

A full-stack **Project Manager** web application built with **Django** and **Bootstrap 5**. It demonstrates complete Create, Read, Update, and Delete (CRUD) workflows using Django `ModelForm`, field-level and cross-field custom validation, flash messaging, and media file handling (PDFs, documents, and images).

---

## Features

- **Full CRUD Operations:** Create, view, update, and delete project records via clean function-based views.
- **ModelForm Integration:** Uses `ProjectForm` with Bootstrap-styled widgets and `ClearableFileInput` for seamless file replacement or retention during edits.
- **Custom Validation Rules:**
  - **Budget Validation:** Ensures the project budget is strictly greater than zero.
  - **File Upload Validation:** Enforces a **5 MB maximum file size** and restricts uploads to `.pdf`, `.docx`, `.png`, `.jpg`, and `.jpeg`.
  - **Cross-Field Validation:** Requires projects with a budget over **$10,000** to include a description of at least **20 characters**.
- **Media Storage & Cleanup:** Stores uploaded proposals in `media/proposals/`, renders direct download/preview links, and automatically deletes orphaned files from disk when a project is deleted.
- **User Feedback:** Displays dismissible Bootstrap alert banners via Django's `messages` framework after create, update, and delete actions.

---

## Tech Stack

- **Backend:** Python 3, Django
- **Frontend:** HTML5, Bootstrap 5.3 (CDN)
- **Database:** SQLite3 (default development database)

---

## Project Structure

```text
django_crud_forms/
├── config/
│   ├── settings.py
│   └── urls.py
├── projects/
│   ├── templates/
│   │   └── projects/
│   │       ├── base.html
│   │       ├── project_list.html
│   │       ├── project_form.html
│   │       └── project_confirm_delete.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/
│   └── proposals/
├── screenshots/
├── db.sqlite3
└── manage.py