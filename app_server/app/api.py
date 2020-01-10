import os
import time

from flask import request, jsonify, g

from app_server.app import blueOne
from app_server.app.logic import FORWARD
from app_server.app.logic import BACKWARD
from app_server.CONSTANT import CODE

from utils.logger import Logger

logger = Logger(__name__)


@blueOne.after_request
def del_wrong_file(response):
    if g.__dict__:
        print(g.name)
        os.remove(g.name)
    # print(globals())
    return response


@blueOne.route("/forward", methods=['post'])
def _forward():
    logger.get_log().info("connect _forward")

    code = request.form.get('code')

    stamp = time.strftime("%Y-%m-%d-%H", time.localtime())
    path = 'static/file/forward_output_%s.csv' % (code + '_' + stamp)
    short_path = '/file/' + os.path.split(path)[-1]
    data = {
        "code": None,
        "path": short_path
    }
    if os.path.exists(path):
        data["code"] = CODE.EXISTS
        return jsonify(data)

    try:
        forward = FORWARD(code, path)
        result = forward.run()
    except Exception as e:
        logger.get_log().debug('forward:' + str(e))
        print(e)

        result = CODE.TYPEERR
    data["code"] = result

    if result != CODE.SUCCESS:
        g.name = path

    return jsonify(data)


@blueOne.route("/backward", methods=['post'])
def _backward():
    logger.get_log().info("connect _backward")
    code = request.form.get('code')
    stamp = time.strftime("%Y-%m-%d-%H", time.localtime())
    path = 'static/file/backward_output_%s.csv' % (code + '_' + stamp)
    short_path = '/file/' + os.path.split(path)[-1]
    data = {
        "code": None,
        "path": short_path
    }
    if os.path.exists(path):
        data["code"] = CODE.EXISTS
        return jsonify(data)

    try:
        back = BACKWARD(code, path)
        result = back.run()

    except Exception as e:
        logger.get_log().debug('backward:' + str(e))
        print(e)
        result = CODE.TYPEERR
    data["code"] = result

    if result != CODE.SUCCESS:
        g.name = path

    return jsonify(data)
