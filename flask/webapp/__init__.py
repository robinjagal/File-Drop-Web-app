from flask import Flask
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()
app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)
app.config['SECRET_KEY'] = "b97c2506aacb7eb4f868406c339adcc16df87271ebb0dfe1"
from webapp import routes

