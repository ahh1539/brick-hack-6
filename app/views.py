from flask import Flask,request,render_template, url_for,redirect
# from flaskext.mysql import MySQL
from app import app



@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid Credentials"
        else:
            return redirect(url_for('index'))
    return render_template("login.html", error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    return render_template("sell.html")

# @app.route('/sell_item', methods=['GET', 'POST'])
# def sell_item():
#     app = Flask(__name__)
#     app.config['MYSQL_DATABASE_USER'] = 'root'
#     app.config['MYSQL_DATABASE_PASSWORD'] = 'Lads69'
#     app.config['MYSQL_DATABASE_HOST'] = '35.243.163.114'
#     app.config['MYSQL_DATABASE_DB'] = 'brick'
#     mysql = MySQL()
#     mysql.init_app(app)
#     Item_Name = request.form['Item_Name']
#     Price = request.form['Price']
#     Description = request.form['Description']
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     query = ("""INSERT INTO items (item_name,price,dets) VALUES(%s,%s,%s)""")
#     cursor.execute(query, (Item_Name,Price,Description))
#     conn.commit()
#     return render_template("created.html")

@app.route('/expanded-card', methods=['GET', 'POST'])
def expanded_card():
    return render_template("card-expanded.html")

# @app.route('/signup-confirmation', methods=['GET', 'POST'])
# def signup_confirm():
#     app = Flask(__name__)
#     app.config['MYSQL_DATABASE_USER'] = 'root'
#     app.config['MYSQL_DATABASE_PASSWORD'] = 'Lads69'
#     app.config['MYSQL_DATABASE_HOST'] = '35.243.163.114'
#     app.config['MYSQL_DATABASE_DB'] = 'brick'
#     mysql = MySQL()
#     mysql.init_app(app)
#     Username = request.form['Username']
#     Password = request.form['Password']
#     Phone_Number = request.form['Phone_Number']
#     Full_Name = request.form['Full_Name']
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     query = ("""INSERT INTO users (username,password,phone_number,full_name) VALUES(%s,%s,%s,%s)""")
#     cursor.execute(query, (Username,Password,Phone_Number,Full_Name))
#     conn.commit()
#     return render_template("sign-up-confirm.html")
