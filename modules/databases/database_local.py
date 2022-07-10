import os
from datetime import datetime
import sqlalchemy as sql
from sqlalchemy.orm import relationship, backref, Session, sessionmaker
import sqlalchemy.ext.declarative as declarative
from sqlalchemy import null, select, update, delete


BASE_DIR = os.path.dirname(__file__)
BASE_DIR = f'{BASE_DIR}/database_local.db'

engine = sql.create_engine(f"sqlite:///{BASE_DIR}")

Base = declarative.declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "user"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    nome = sql.Column(sql.String(50), index=True, )
    tecnologia = sql.Column(sql.String(50), index=True)


class Mensagens(Base):
    __tablename__ = "mensagens"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    texto = sql.Column(sql.String(2000), index=True)
    nome = sql.Column(sql.String(50), index=True)
    tecnologia = sql.Column(sql.String(50), index=True)
    

def add_tables():
    Base.metadata.create_all(bind=engine)

def add_user_local(nome, tecnologia):
    session.query(User).filter(User.id == 1).update(
        {
            'nome': nome,
            'tecnologia': tecnologia
        }
    )

    session.commit()
    session.flush()

def is_user(datas=None):
    query = session.query(User).first()
    session.commit()
    
    if datas:
        return query
    else:
        if query.nome:
            return True
        else:
            return False

