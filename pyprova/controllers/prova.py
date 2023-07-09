import traceback

from flask import Blueprint, request, app
from ..models.user import User
from ..services.prova import *

prova = Blueprint('prova', __name__, url_prefix='/prova/<prova_id>')
questao = Blueprint('questao', __name__, url_prefix='questao/<questao_id>')

prova.register_blueprint(questao)


@prova.route('/<method>', methods=['POST'])
def modify_prova(prova_id, method):
    try:
        data = request.json
        # TODO: get current user pass as professor
        prova_data = {'id': prova_id, 'inicio': data['inicio'], 'fim': data['fim'], 'professor': None}

        if method == 'create':
            message = create_prova(prova_data)
        elif method == 'update':
            message = update_prova(prova_data)
        elif method == 'delete':
            message = delete_prova(prova_id)
        elif method == 'register' and "current_user.tipo" == 'aluno':
            register_prova(prova_id, "current_user.id")
        else:
            raise(f"Method {method} do not exist!")
    except Exception as e:
        return {'success': False, 'message': traceback.format_exc()}
    return {'success': True, 'message': message}


@prova.route('/', methods=['GET'])
def show_prova(prova_id):
    try:
        # TODO: get current user
        if "current_user.tipo" == 'professor':
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
        # TODO: get current user pass as professor
        questao_data = {'id': questao_id, 'prova': prova_id, 'tipo': data['tipo'], 'comando': data['comando'],
                        'opcoes': data['opcoes'], 'gabarito': data['gabarito'], 'valor': data['valor']}

        if method == 'create':
            message = create_questao(questao_data)
        elif method == 'update':
            message = update_questao(questao_data)
        elif method == 'delete':
            message = delete_questao(questao_data)
        else:
            raise(f"Method {method} do not exist!")
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
