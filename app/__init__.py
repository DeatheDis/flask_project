from flask import Flask
import os

SECRET_KEY = os.getenv('SECRET_KEY')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
from app import routes