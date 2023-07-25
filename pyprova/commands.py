import datetime
import click


from .extensions import db
from flask.cli import with_appcontext
from .models.prova import *
from werkzeug.security import generate_password_hash, check_password_hash

@click.command()
@with_appcontext
def seed():
    pedro = User(id=1, name="pedro", email="pedro@unb.br", password=generate_password_hash("asdfg", method='sha256'), profile_type=1)
    ester = User(id=2, name="ester", email="ester@unb.br", password=generate_password_hash("asdfg", method='sha256'), profile_type=2)

    # Provas fechadas
    provaf_sem = Prova(id=1, professor=pedro.id, inicio=datetime.datetime(2022, 7, 25, 18, 27, 13, 150106), fim=datetime.datetime(2022, 7, 25, 18, 27, 13, 150106))
    provaf_com = Prova(id=2, professor=pedro.id, inicio=datetime.datetime(2022, 7, 25, 18, 27, 13, 150106),
                       fim=datetime.datetime(2022, 7, 25, 18, 27, 13, 150106))


    # Provas abertas
    provaa_sem = Prova(id=3, professor=pedro.id, inicio=datetime.datetime(2022, 7, 25, 18, 27, 13, 150106),
                       fim=datetime.datetime(2024, 7, 25, 18, 27, 13, 150106))
    provaa_com = Prova(id=4, professor=pedro.id, inicio=datetime.datetime(2022, 7, 25, 18, 27, 13, 150106),
                       fim=datetime.datetime(2024, 7, 25, 18, 27, 13, 150106))

    prova_agendada = Prova(id=5, professor=pedro.id, inicio=datetime.datetime(2024, 7, 25, 18, 27, 13, 150106),
                       fim=datetime.datetime(2024, 7, 25, 18, 27, 13, 150106))

    db.session.add_all([pedro,ester,provaf_sem,provaf_com,provaa_sem,provaa_com,prova_agendada])


    # Questoes + inscricao
    for p in range(1,5):
            q1 = Questao(id=10*p+1, prova=p, tipo='vf', comando="Essa questão é de tipo numérico", opcoes='Verdadeiro;;Falso', gabarito='Falso', valor=1)
            q2 = Questao(id=10*p+2, prova=p, tipo='mul', comando="Quantos opcoes essa questão tem?",
                        opcoes='1;;2;;3', gabarito='3', valor=1)
            q3 = Questao(id=10*p+3, prova=p, tipo='num', comando="Quanto vale essa questão?",
                        opcoes='', gabarito=2, valor=2)
            i = Inscricao(id=p,aluno=ester.id,prova=p)
            db.session.add_all([q1,q2,q3,i])


    # Respostas
    r1 = Resposta(id=1, questao=21, aluno=ester.id, resposta='Verdadeiro')
    r2 = Resposta(id=2, questao=22, aluno=ester.id, resposta='3')
    r3 = Resposta(id=3, questao=23, aluno=ester.id, resposta=2)

    r4 = Resposta(id=4, questao=41, aluno=ester.id, resposta='Verdadeiro')
    r5 = Resposta(id=5, questao=42, aluno=ester.id, resposta='3')
    r6 = Resposta(id=6, questao=43, aluno=ester.id, resposta=2)

    db.session.add_all([r1, r2, r3, r4, r5, r6])
    db.session.commit()