from flask import Flask
from Routes import API
from flask_cors import CORS
from flask_socketio import SocketIO
import Controller

socketio = SocketIO()


def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug
    CORS(app)
    app.register_blueprint(API.mod)
    socketio.init_app(app)
    return app
