from flask import jsonify

from .. import db
from ..models.user import User
from ..models.prova import Prova, Questao, Resposta, Inscricao

date_format = '%Y-%m-%dT%H:%M'

def create_prova(prova_data):
    new_prova = Prova(professor=prova_data['professor'], inicio=prova_data['inicio'], fim=prova_data['fim'])
    db.session.add(new_prova)
    db.session.commit()

    return 'Prova successfully created!'


def update_prova(prova_data):
    prova = Prova.query.filter_by(id=prova_data['id']).first()

    if prova:
        prova.inicio = prova_data['inicio']
        prova.fim = prova_data['fim']
        db.session.commit()

        return 'Update successful!'
    raise Exception('Prova not found!')


def delete_prova(prova_id):
    prova = Prova.query.filter_by(id=prova_id).first()

    if prova:
        db.session.delete(prova)
        db.session.commit()

        return 'Deletion successful!'
    raise Exception('Prova not found!')


def index_provas(id, tipo):
    if tipo == 1:
        return index_provas_professor(id)
    elif tipo == 2:
        return index_provas_aluno(id)
    raise Exception("Tipo de usuario invalido!")


def index_provas_professor(id):
    message = {'provas': []}

    provas = Prova.query.filter_by(professor=id)

    for p in provas:
        prova = {'id': p.id, 'inicio': p.inicio.strftime(date_format), 'fim': p.fim.strftime(date_format)}
        message['provas'].append(prova)
    message['edit'] = True
    return message


def index_provas_aluno(id):
    message = {'provas': []}

    inscricoes = Inscricao.query.filter_by(aluno=id)

    for i in inscricoes:
        p = Prova.query.filter_by(id=i.prova).first()
        prova = {'id': p.id, 'inicio': p.inicio.strftime(date_format), 'fim': p.fim.strftime(date_format)}
        message['provas'].append(prova)
    message['edit'] = False
    return message


def create_questao(questao_data):
    opcoes = questao_data['opcoes']
    if questao_data['tipo'] == 'vf':
        opcoes = ['Verdadeiro', 'Falso']
    opcoes = ";;".join(opcoes)
    new_questao = Questao(prova=questao_data['prova'], tipo=questao_data['tipo'], comando=questao_data['comando'],
                          opcoes=opcoes, gabarito=questao_data['gabarito'], valor=questao_data['valor'])
    db.session.add(new_questao)
    db.session.commit()


def update_questao(questao_data):
    questao = Questao.query.filter_by(id=questao_data['id']).firtst()
    if questao:
        questao.comando = questao_data['comando']
        opcoes = ";;".join(questao_data['opcoes'])
        questao.opcoes = opcoes
        questao.gabarito = questao_data['gabarito']
        questao.valor = questao_data['valor']
        db.session.commit()
        return 'Update successful!'
    raise Exception('Questao not found!')


def delete_questao(questao_data):
    questao = Questao.query.filter_by(id=questao_data['id']).firtst()
    if questao:
        db.session.delete(questao)
        db.session.commit()
        return 'Update successful!'
    raise Exception('Questao not found!')


def get_questoes(prova_id, show_ans=False):
    message = {'questoes': []}
    questoes = Questao.query.filter_by(prova=prova_id)

    for q in questoes:
        questao = {'id': q.id,
                   'tipo': q.tipo,
                   'comando': q.comando,
                   'opcoes': q.opcoes.split(';;'),
                   'valor': q.valor,
                   'gabarito': None,
                   'resposta': None}
        if show_ans:
            questao['gabarito'] = q.gabarito
        message['questoes'].append(questao)

    return message


def detail_questao(questao_id):
    q = Questao.query.filter_by(id=questao_id)

    if not q:
        raise("Questao not found!")

    questao = {'id': q.id,
                   'tipo': q.tipo,
                   'comando': q.comando,
                   'opcoes': q.opcoes.split(';;'),
                   'valor': q.valor,
                   'gabarito': q.gabarito}
    return {'questao' : questao}


def create_respostas(aluno_id, prova_id):
    questoes = Questao.query.filter_by(prova=prova_id)
    respostas = []

    for q in questoes:
        new_resposta = Resposta(prova=prova_id, questao=q.id, aluno=aluno_id, resposta = '')
        respostas.append(new_resposta)

    db.session.add_all(respostas)
    db.session.commit()


def update_resposta(resposta_data):
    resposta = Resposta.query.filter_by(aluno=resposta_data['aluno'], questao=resposta_data['questao']).first()
    resposta.resposta = resposta_data['resposta']
    db.session.commit()
    return "Resposta updated successfully!"


def check_num(gabarito,resposta):
    if float(gabarito) == float(resposta):
        return True
    return False


# V e F é considerada uma questão múltipla escolha para checar seguindo filosofia DRY
def check_option(gabarito,resposta):
    if gabarito == resposta:
        return True
    return False


# Passar resultado de query para a funcao
def check_ans(resposta):
    if resposta.questao.tipo == 'num':
        return check_num(resposta.questao.gabarito, resposta.resposta)
    if resposta.questao.tipo == 'vf' or resposta.questao.tipo == 'option':
        return check_option(resposta.questao.gabarito, resposta.resposta)



def gen_feedback_individual(aluno_id, prova_id):
    message = get_questoes(prova_id, show_ans=True)
    message['total'] = 0
    message['nota'] = 0

    for q in message['questoes']:
        resposta = Resposta.query.filter_by(questao=q['id'], aluno=aluno_id)
        q['resposta'] = resposta.resposta
        q['correct'] = False
        message['total'] += q.valor
        if check_ans(resposta):
            message['nota'] += q.valor
            q['correct'] = True

    return message



def gen_feed_back(prova_id):
    inscritos = Inscricao.query.filter_by(prova=prova_id)
    inscritos = [i.aluno for i in inscritos]

    alunos = {}

    for i in inscritos:
        alunos[i.id] = gen_feedback_individual(aluno_id=i.id, prova_id=prova_id)

    return alunos

def register_prova(prova_id, aluno_id):
    p = Prova.query.filter_by(id=prova_id).first()
    if not p:
        raise Exception("Codigo invalido!")

    inscricao = Inscricao.query.filter_by(aluno=aluno_id)
    inscricao = inscricao.filter_by(prova=prova_id).first()

    if not inscricao:
        new_inscricao = Inscricao(aluno=aluno_id, prova=prova_id)
        db.session.add(new_inscricao)
        db.session.commit()
        create_respostas(aluno_id,prova_id)
        return "Inscricao Concluida!"
    raise Exception("Inscicao repetida!")

