# NECYSC App

## Getting Started.

Django is a Model-View-Template (MVT) framework that allows you to build web applications. It is a high-level Python web framework that encourages rapid development and clean, pragmatic design. This means that developers will be either working on the models, the views, or the templates. The models are the database, the views are the logic and processing, and the templates are the frontend.

1. Read the documentation: [Documentation](https://docs.djangoproject.com/en/5.1/intro/overview/)

2. Ensure Python 3.11+ is installed on your machine. If not, download it from [Python](https://www.python.org/downloads/)

3. Install Django using pip. Run the following command in your terminal. Create a virtual environment if you want to.

```bash
    pip install -r requirements.txt
```

4. Run the server.

```bash
    python manage.py runserver
```

5. Open your browser and go to `http://localhost:8080/necysc_app`

6. To access the admin panel, go to `http://localhost:8080/admin` and login with the following credentials:

```bash
    username: admin
    password: password
```

7. To create a superuser, run the following command in your terminal.

```bash
    python manage.py createsuperuser
```

8. To make migrations (updating the database column headers if you change the models), run the following command in your terminal.

```bash
    python manage.py makemigrations
    python manage.py migrate
```

9. An example codebase for another website I previously worked on: https://github.com/charlestang06/tutoring-app/tree/master

## Tech Stack

- **Frontend**: HTML, CSS (Bootstrap 5.0), JavaScript
- **Backend**: Django, MySQL
- **Deployment**: Python 3.11.5, WSGI

## Features

When creating a new feature, create a new view and a new template. Add the view to the `urls.py` file in the `necysc_app` folder.

- Setting up Model for Applicants (features)
- Setting up the Applicant Registration Form
- Landing page
- Registration pages
- Login page
- Admin dashboard

## How To Run

We assume you have the latest version of Python installed.

1. Clone the repository

```bash
    git clone
```

2. Install the required packages

```bash
    pip install django
```

3. Make migrations

```bash
    python manage.py makemigrations
    python manage.py migrate
```

4. Run the server.

```bash
    python manage.py runserver 8080
```

5. Open your browser and go to `http://localhost:8080/`
