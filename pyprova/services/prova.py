from .. import db
from ..models.user import User
from ..models.prova import Prova, Questao, Resposta

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
    return  'Prova not found!'


def delete_prova(prova_data):
    prova = Prova.query.filter_by(id=prova_data['id']).first()

    if prova:
        db.session.delete(prova)
        db.session.commit()

        return 'Deletion successful!'
    return 'Prova not found!'


def create_questao(questao_data):
    pass


def update_questao(questao_data):
    pass


def delete_questao(questao_data):
    pass


def get_questoes(prova_id, show_ans=False):
    message = {'questoes': []}
    questoes = Questao.query.filter_by(prova=prova_id)

    for q in questoes:
        questao = {'id': q.id,
                   'tipo': q.tipo,
                   'comando': q.comando,
                   'opcoes': q.opcoes.split(';;'),
                   'valor': q.valor,
                   'gabarito': None}
        if show_ans:
            questao['gabarito'] = q.gabarito
        message['questoes'].append(questao)

    return message


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


# Recebe json gerado por feedback individual
def calculate_grade(ans_json):
    pass


def gen_feedback_individual(aluno_id, prova_id):
    pass


def gen_feed_back(prova_id):
    pass