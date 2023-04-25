from flask import jsonify, Blueprint
from libs.random.random import Random

foo_module = Blueprint("foo", __name__, url_prefix='/foo')

@foo_module.route("/", methods=["GET"])
def get():
    data = {
        'foo': 'bar',
        "int": Random.get_random_int(),
    }
    return jsonify(data)
