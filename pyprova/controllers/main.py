import traceback

from flask import Blueprint, jsonify
from .. import db
from ..services.prova import *


main = Blueprint('main', __name__)

@main.route('', methods=['GET'])
def index_provas():
    try:
        message = index_provas("current_user.id", "current_user.tipo")
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}
