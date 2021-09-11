from flask import Flask, render_template
import pymysql.cursors
app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='35.238.255.61',
                             user='root',
                             password='claimcart',
                             db='claims',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

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
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `*` FROM `items` WHERE `user`=%s"
        cursor.execute(sql, ('ayushdewan02@gmail.com',))
        result = cursor.fetchall()
        for i in result:
            i['price'] = "$%0.2f" % i['price']
    print(result)
    return render_template("dashboard.html", username=username.capitalize(), table=result)