from ..extensions import db
from .user import User

class Prova(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    inicio = db.Column(db.DateTime)
    fim = db.Column(db.DateTime)

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prova = db.Column(db.ForeignKey(Prova.id, ondelete='CASCADE'))
    tipo = db.Column(db.String(100))
    comando = db.Column(db.String(2000))
    opcoes = db.Column(db.String(2000))
    gabarito = db.Column(db.String(1000))
    valor = db.Column(db.Integer)


class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao = db.Column(db.ForeignKey(Questao.id, ondelete='CASCADE'))
    aluno = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    resposta = db.Column(db.String(1000))


class Inscricao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    prova = db.Column(db.ForeignKey(Prova.id, ondelete='CASCADE'))
