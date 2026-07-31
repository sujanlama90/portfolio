# 🎨 Django Portfolio

A clean, responsive personal portfolio website built with Django, HTML, CSS and Bootstrap. This beginner-friendly project showcases Home, About, Projects, Blog and Contact sections and uses SQLite for simple data persistence.

---

## Features

- Professional, minimal design with responsive layout
- Home, About, Projects, Blog and Contact pages
- Contact form (sends/stores messages via Django — configure as needed)
- Projects gallery with images and descriptions
- Blog listing and detail pages (basic CMS-style posts)
- Static assets using organized `static/` folder
- Uses SQLite for lightweight, zero-config development

## Technologies

- Django
- Python
- HTML5
- CSS3
- Bootstrap
- SQLite

## Project Structure

Top-level layout of this repository:

```
portfolio_project/
    db.sqlite3
    manage.py
    myPortfolio/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        migrations/
        static/
            css/
                style.css
            js/
                script.js
            images/
        templates/
            base.html
            home.html
            about.html
            projects.html
            blog.html
            contact.html
            resume.html
    portfolio_project/
        settings.py
        urls.py
        wsgi.py
        asgi.py
```

Adjust paths if you customize the app name or layout.

## Installation (local development)

1. Clone the repository

```bash
git clone https://github.com/sujanlama90/portfolio.git
cd portfolio_project
```

2. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If not, install Django (example):

```bash
pip install django
```

4. Apply database migrations

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Environment & Configuration

- This project uses SQLite by default (db.sqlite3 in project root).
- For production use, configure `DATABASES` in `portfolio_project/settings.py` and set `DEBUG = False`.
- Add environment variable handling for secrets (e.g., `DJANGO_SECRET_KEY`, SMTP credentials) before deploying.

## Contact

If you have questions or suggestions, reach out:

- Email: sujanlama2323@gmail.com
- GitHub: https://github.com/sujanlama90

## Future Improvements

- Add deployment instructions (Heroku / DigitalOcean / Vercel + WSGI/ASGI config)
- Add unit and integration tests for views and forms
- Add CI (GitHub Actions) for linting, testing and automated deploys

## License

This project is licensed under the MIT License — see the LICENSE file for details.

If you prefer a different license, replace this section and add a `LICENSE` file.

---

Thank you for checking out this portfolio project. Customize the content, design and sections to make it your own!
