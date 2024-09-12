## ResumeProcessor_A
Extracting user email ,name and mobile no from resume
# Overview
This project is a Django-based REST API designed to extract specific information (first name, email ID, and mobile number) from a candidate's resume (in PDF or Word format). It utilizes Python libraries to parse the resume and process the data.

# Project Setup
Prerequisites
Python 3.x
PostgreSQL
Django 4.x
Django REST Framework
Pyresparser (or an alternative NLP tool for parsing resumes)
Any required AI tools (optional)
Installation Steps


-> Clone the repository:

git clone <your-git-repo-url>
cd ResumeProcessor
Set up a virtual environment:

python3 -m venv myenv

source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate  # Windows

# Install the dependencies:

pip install -r requirements.txt
Database Setup:

Make sure PostgreSQL is installed and running.

# Create a PostgreSQL database:

Copy code
CREATE DATABASE resume_processor;
CREATE USER resume_user WITH PASSWORD 'yourpassword';
ALTER ROLE resume_user SET client_encoding TO 'utf8';
ALTER ROLE resume_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE resume_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE resume_processor TO resume_user;
Configure the Django Project:

# Update your settings.py to include the PostgreSQL database configuration:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume_processor',
        'USER': 'resume_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Run database migrations:


python manage.py migrate

# Run the server:
python manage.py runserver

Usage
select resume file and upload it it will redirect to 
API Endpoint
Endpoint: /api/extract_resume/

Method: POST

Request Body: A resume file in either PDF or Word format.

Response Example:
{
    "first_name": "Avani Kathiriya",
    "email": "avanikathiriya24@gmail.com",
    "mobile_number": "123-456-7890"
}
it will store the data in database.
