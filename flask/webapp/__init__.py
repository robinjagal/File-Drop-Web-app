from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "b97c2506aacb7eb4f868406c339adcc16df87271ebb0dfe1"

from webapp import routes