from flask import Blueprint, jsonify
from .. import db


main = Blueprint('main', __name__)

@main.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
