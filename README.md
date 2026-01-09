# Bank App

A simple web CRUD app for managing banks, build with Flask and MySQL.
It allow users to:

- Add new banks
- Vies a list of banks
- View details of a specific bank
- Edit bank information
- Delete banks

## Technologies Used

- Python 3
- Flask
- MySQL
- HTML
- Pytest

## Project Structure

bank_app/
----app.py # Main Flask application
----config.py # MySQL configuration
----test_app.py # Pytest file
----requirements # Project dependencies
----templates/ # HTML templates
    ----home.page.html
    ----add_banks.html
    ----list_banks.html
    ----bank_details.html
    ----edit_bank.html

## Setup Instructions

1. Create a virtual enviroment
    python3 -m venv venv
    source venv/bin/activate

2. Install dependencies
    pip install -r requirements.txt
    
3. Set up MySQL database
    CREATE DATABASE bank_db;
    USE bank_db;
    CREATE TABLE banks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        location VARCHAR(100)
    );

4. Configure your credentials in config.py
    class Config:
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'your_user'
        MYSQL_PASSWORD = 'your_password'
        MYSQL_DB = 'BankDB'
        MYSQL_CURSORCLASS = 'DictCursor'

5. Run the Application
    python3 app.py
    




