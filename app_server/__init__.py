from flask import Flask
from app_server.app.api_v1 import api_v1_blue
from app_server.app.api_v2 import api_v2_blue

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_v1_blue)
    app.register_blueprint(api_v2_blue)


    return app

