from flask import render_template, url_for

from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


