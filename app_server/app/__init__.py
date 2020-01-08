from flask import Blueprint

blueOne = Blueprint('app1', __name__)


from . import api
