import traceback

from flask import Blueprint, request, app
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from datetime import datetime
from ..models.user import User
from ..services.auth import get_user_by_email
from ..services.prova import *

prova = Blueprint('prova', __name__, url_prefix='/prova/<prova_id>')
questao = Blueprint('questao', __name__, url_prefix='questao/<questao_id>')

prova.register_blueprint(questao)


@prova.route('/<method>', methods=['POST'])
@jwt_required()
def modify_prova(prova_id, method):
    try:
        date_format = '%Y-%m-%dT%H:%M'
        data = request.json
        user = get_user_by_email(get_jwt_identity())
        if data['inicio'] or data['fim']:
            prova_data = {'id': prova_id, 'inicio': datetime.strptime(data['inicio'], date_format), 'fim': datetime.strptime(data['fim'], date_format), 'professor': user.id}

        if method == 'create':
            message = create_prova(prova_data)
        elif method == 'update':
            message = update_prova(prova_data)
        elif method == 'delete':
            message = delete_prova(prova_id)
        elif method == 'register' and user.profile_type == 2:
            message = register_prova(prova_id, user.id)
        else:
            raise Exception(f"Method {method} do not exist!")
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}


@prova.route('', methods=['GET'])
@jwt_required()
def show_prova(prova_id):
    try:
        user = get_user_by_email(get_jwt_identity())
        if user.profile_type == 1:
            message = get_questoes(prova_id=prova_id, show_ans=True)
            message['edit'] = True
        else:
            message = get_questoes(prova_id=prova_id)
            message['edit'] = False
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}


@questao.route('/<method>', methods=['POST'])
def modify_questao(prova_id, questao_id, method):
    try:
        data = request.json
        questao_data = {'id': questao_id, 'prova': prova_id, 'tipo': data['tipo'], 'comando': data['comando'],
                        'opcoes': data['opcoes'], 'gabarito': data['gabarito'], 'valor': data['valor']}

        if method == 'create':
            message = create_questao(questao_data)
        elif method == 'update':
            message = update_questao(questao_data)
        elif method == 'delete':
            message = delete_questao(questao_data)
        elif method == 'detail':
            message = detail_questao(questao_id)
        else:
            raise Exception(f"Method {method} do not exist!")
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}


@prova.route('/review', methods=['GET'])
def review_prova(prova_id):
    try:
        # TODO: get current user
        if "current_user.tipo" == 'professor':
            message = gen_feed_back(prova_id)
            message['tipo'] = 'professor'
        else:
            message = gen_feedback_individual(prova_id, "current_user.id")
            message['tipo'] = 'aluno'
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}


@questao.route('/responder', methods=['POST'])
def responder(prova_id, questao_id):
    try:
        data = request.json
        resposta_data = {'questao': questao_id, 'resposta': data['resposta'], 'aluno': "current_user"}
        message = update_resposta(resposta_data)
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}
