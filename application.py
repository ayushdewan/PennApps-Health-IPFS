from flask import Flask, render_template
import pymysql.cursors
app = Flask(__name__)


# Login Page
@app.route('/')
def index():
    return render_template("login.html")

# Dashboard Page
@app.route('/user/<username>')
def show_dash(username):
    return render_template("dashboard.html", username=username.capitalize(), table=[])

# List Page
@app.route('/list/<username>')
def show_list(username):
    result = []
    return render_template("dashboard.html", username=username.capitalize(), table=result)