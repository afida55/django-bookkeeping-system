# Bookkeeping Management System

A web-based bookkeeping application developed with Django and MySQL to help users manage and track their financial records.

## Features

- User registration and login
- Income and expense record management
- Category management
- Financial statistics and summaries
- User profile management
- MySQL database integration

## Technologies Used

- Python
- Django
- MySQL
- HTML and CSS
- JavaScript

## Requirements

- Python
- MySQL Server
- pip

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/afida55/django-bookkeeping-system.git
cd django-bookkeeping-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root, in the same directory as `manage.py`.

Add your own values:

```env
DJANGO_SECRET_KEY=replace_with_a_new_secret_key
DJANGO_DEBUG=True

MYSQL_DATABASE=chapt15
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
```

Replace the example values with your own configuration. Never upload your `.env` file or real credentials to GitHub.

### 5. Create the MySQL database

Create a database matching the `MYSQL_DATABASE` value in your `.env` file. For example:

```sql
CREATE DATABASE chapt15;
```

Make sure your MySQL server is running and the configured user has permission to access the database.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Security Notes

- Keep `.env` out of version control.
- Use your own Django secret key and database credentials.
- Set `DJANGO_DEBUG=False` when deploying to production.
- Configure `ALLOWED_HOSTS` appropriately before production deployment.

## Author

Aktar Most Afida

GitHub: https://github.com/afida55
