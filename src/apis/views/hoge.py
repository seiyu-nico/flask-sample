from flask import jsonify, Blueprint
from libs.random.random import Random

hoge_module = Blueprint("hoge", __name__, url_prefix='/hoge')

@hoge_module.route("/", methods=["GET"])
def get():
    data = {
        'hoge': 'piyo',
        "int": Random.get_random_int(),
    }
    return jsonify(data)
