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
    texto = sql.Column(sql.String(2000), index=True)
    nome = sql.Column(sql.String(50), index=True)
    tecnologia = sql.Column(sql.String(50), index=True)
    

def add_tables():
    Base.metadata.create_all(bind=engine)


