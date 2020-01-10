from flask import Flask

from app_server.app import blueOne
from app_server import web_html
from utils.commoms import ReConverter
from app_server.web_html import *


def create_app():
    app = Flask(__name__, static_folder='static', root_path='')
    app.debug = True
    app.secret_key = 'SADJHASIUDQPIWDPH903'

    app.url_map.converters['re'] = ReConverter

    # 注册蓝图
    # CSRFProtect(app)

    app.register_blueprint(blueOne)
    app.register_blueprint(web_html.html)

    return app
