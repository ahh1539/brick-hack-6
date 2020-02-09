from flask import render_template, url_for, redirect, request

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

