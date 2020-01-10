from flask import Blueprint

blueOne = Blueprint('app1', __name__)

from app_server.app import api
