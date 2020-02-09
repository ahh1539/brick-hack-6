from flask import Flask
# from flask_sqlalchemy import 

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# , static_url_path='', static_folder='static',template_folder='app/templates'


# Load the views
from app import views

# Load the config file
app.config.from_object('config')

# def clever_function():
#     return u'HELLO'

# app.jinja_env.globals.update(clever_function=clever_function)