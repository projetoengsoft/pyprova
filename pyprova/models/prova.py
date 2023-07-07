from .. import db
from .user import User

class Prova(db.model):
    id = db.Column(db.Integer, primary_key=True)
    professor = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    inicio = db.Column(db.DateTime)
    fim = db.Column(db.DateTime)

class Questao(db.model):
    id = db.Column(db.Integer, primary_key=True)
    prova = db.Column(db.ForeignKey(Prova, ondelete='CASCADE'))
    tipo = db.Column(db.String(100))
    comando = db.Column(db.String(2000))
    opcoes = db.Column(db.String(2000))
    gabarito = db.Column(db.String(1000))
    valor = db.Column(db.Integer)


class Resposta(db.model):
    id = db.Column(db.Integer, primary_key=True)
    prova = db.Column(db.ForeignKey(Prova, ondelete='CASCADE'))
    questao = db.Column(db.ForeignKey(Questao, ondelete='CASCADE'))
    aluno = db.Column(db.ForeignKey(User.id))
    resposta = db.Column(db.String(1000))