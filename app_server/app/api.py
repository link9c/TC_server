from flask import request, jsonify

from app_server.app import blueOne
from .logic import forward


@blueOne.route("/forward", methods=['post'])
def p():
    code = request.form.get('code')
    forward(code)
    return jsonify({1: "OK"})
