from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from config import Config

# Create and adjusting Flask App
app = Flask(__name__)
# Input settings from the config file
app.config.from_object(Config)

# Connect MySQL with Flask MySQLdb
mysql = MySQL(app)


# Create a Home Page
@app.route('/')
def homePage():
    return render_template("homePage.html")


# Route for adding new bank into the database
@app.route("/add", methods=['GET', 'POST'])
def add_bank():
    if request.method == 'POST':    # Post method, submitted
        name = request.form['name']  # Load name from the form
        location = request.form['location']  # Load location from the form

        # Perform SQL queries for data entry
        cur = mysql.connection.cursor()
        query = ("INSERT INTO banks (name, location) VALUES (%s, %s)")
        cur.execute(query, (name, location))
        mysql.connection.commit()   # Save changes
        cur.close()

        return redirect(url_for("list_banks"))
    return render_template("add_bank.html")


# Route for list all banks
@app.route('/banks')
def list_banks():
    cur = mysql.connection.cursor()  # Create crud for SQL query
    cur.execute("SELECT * FROM banks")
    banks = cur.fetchall()
    cur.close()
    return render_template("list_banks.html", banks=banks)


# Route for listing bank details
@app.route("/banks/<int:id>")
def bank_details(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM banks WHERE id = %s", (id,))
    bank = cur.fetchone()
    cur.close()
    if bank:
        return render_template("bank_details.html", bank=bank)
    else:
        return "Bank not found", 404  

   
# Route for update the data if necessary
@app.route("/banks/edit/<int:id>", methods=['GET', 'POST'])
def edit_bank(id):
    cur = mysql.connection.cursor()

    # If method is GET show the data
    if request.method == "GET":
        cur.execute("SELECT * FROM banks WHERE id = %s", (id,))
        bank = cur.fetchone()
        cur.close()
        if bank:
            return render_template("edit_bank.html", bank=bank)
        else:
            return "Bank not found", 404
    
    # If method is POST, update the data
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']

        # Update the data
        query = "UPDATE banks SET name = %s, location = %s WHERE id = %s"
        cur.execute(query, (name, location, id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for("list_banks"))


@app.route('/banks/delete/<int:id>', methods=['POST'])
def delete_bank(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM banks WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('list_banks'))


if __name__ == '__main__':
    app.run(debug=True)
