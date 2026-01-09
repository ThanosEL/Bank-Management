# Bank App

A simple **CRUD web application** for managing banks, built with **Flask** and **MySQL**.
This project demonstrates fundamental backend development concepts including routing,
database interaction, templating, configuration management, and automated testing.

---

## 📌 Features

The application allows users to:

- Add new banks
- View a list of all banks
- View detailed information for a specific bank
- Edit existing bank records
- Delete bank entries

---

## 🛠 Technologies Used

- **Python 3**
- **Flask**
- **MySQL**
- **HTML (Jinja2 Templates)**
- **Pytest**

---

## Setup Instructions

1. Create a virtual enviroment
    python3 -m venv venv
    source venv/bin/activate

2. Install dependencies
    pip install -r requirements.txt
    
3. Set up MySQL database
    '''sql
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


