import traceback

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from .. import db
from ..services.prova import *
from ..services.auth import get_user_by_email


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@jwt_required()
def provas():
    try:
        user = get_user_by_email(get_jwt_identity())
        message = index_provas(user.id, user.profile_type)
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}
