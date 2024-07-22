Airflow Project
This repository contains a project configured with Apache Airflow, a platform to programmatically author, schedule, and monitor workflows.

Table of Contents
Getting Started
Prerequisites
Installation
Database Setup
Running the Application
Troubleshooting
Contributing
License
Getting Started
These instructions will help you set up and run the project on your local machine for development and testing purposes.

Prerequisites
Ensure you have the following installed on your system:

Python 3.11
Virtualenv
SQLite (or another database system you're using)
Installation
Clone the repository:

bash
Copier le code
git clone https://github.com/gaelmahe1/airflow.git
cd airflow
Create and activate a virtual environment:

bash
Copier le code
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required packages:

bash
Copier le code
pip install -r requirements.txt
Database Setup
Initialize the database:

bash
Copier le code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Ensure the SQLALCHEMY_DATABASE_URI in your configuration file points to your SQLite database (or the database system you're using).

If you encounter the error no such table: session, create the missing table:

sql
Copier le code
CREATE TABLE session (
  id INTEGER PRIMARY KEY,
  session_id TEXT NOT NULL,
  data TEXT,
  expiry DATETIME
);
Running the Application
Run the Airflow web server:

bash
Copier le code
airflow webserver -p 8080
Run the Airflow scheduler:

bash
Copier le code
airflow scheduler
Open your web browser and navigate to http://127.0.0.1:8080/ to see the Airflow dashboard.

Troubleshooting
Common Issues
sqlite3.OperationalError: no such table: session
If you encounter this error, it means that the session table is missing from your database. Ensure you have run the database migration commands correctly. You can manually create the table using the provided SQL command above.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

