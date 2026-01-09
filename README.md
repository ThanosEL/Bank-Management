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


---

## 🗄 Database Schema

The application uses a MySQL database with the following schema:

''' sql
CREATE DATABASE bank_db;
USE bank_db;

CREATE TABLE banks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

---

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/bank_app.git
cd bank_app

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database Credentials

Edit config.py and update your MySQL credentials:

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'your_user'
    MYSQL_PASSWORD = 'your_password'
    MYSQL_DB = 'bank_db'
    MYSQL_CURSORCLASS = 'DictCursor'

5️⃣ Run the Application
python3 app.py

