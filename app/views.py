from flask import render_template, url_for

from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    return render_template("sell.html")