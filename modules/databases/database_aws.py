import os
import sqlalchemy as sql
from sqlalchemy.orm import relationship, backref, Session, sessionmaker
import sqlalchemy.ext.declarative as declarative
from sqlalchemy import null, select, update, delete

BASE_DIR = os.path.dirname(__file__)
engine = sql.create_engine("mysql+pymysql://admin:842684265@database.c4qq48rdfit7.us-east-1.rds.amazonaws.com/chat")

Base = declarative.declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    nome = sql.Column(sql.String(50), index=True, )
    tecnologia = sql.Column(sql.String(50), index=True)
    online = sql.Column(sql.Boolean, index=True)
    reports = sql.Column(sql.Integer, index=True)
    acesso = sql.Column(sql.Boolean, index=True)

class Mensagens(Base):
    __tablename__ = "mensagens"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    nome = sql.Column(sql.String(50), index=True, )
    texto = sql.Column(sql.String(200), index=True)

class FeedBack(Base):
    __tablename__ = "feedbacks"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    nome = sql.Column(sql.String(50), index=True)
    texto = sql.Column(sql.String(2000), index=True)


def add_tables():
    Base.metadata.create_all(bind=engine)

def add_user(nome, tecnologia, online, reports, acesso):
    dados = User(
        nome=nome,
        tecnologia=tecnologia,
        online=online,
        reports=reports,
        acesso=acesso,)

    session.add(dados)
    session.commit()
    session.flush()

def list_users(completo=None):
    query = session.query(User).all()
    session.commit()

    users = []
    if completo:
        return query
    else:
        for user in query:
            users.append(user.nome)

    return users

def add_feedback(nome, texto):
    dados = FeedBack(
        nome=nome,
        texto=texto)

    session.add(dados)
    session.commit()
    session.flush()

def add_messages(nome, texto):
    dados = Mensagens(
        nome=nome,
        texto=texto
    )
    session.add(dados)
    session.commit()
    session.flush()
