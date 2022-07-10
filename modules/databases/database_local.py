import os
from datetime import datetime
import sqlalchemy as sql
from sqlalchemy.orm import relationship, backref, Session, sessionmaker
import sqlalchemy.ext.declarative as declarative
from sqlalchemy import null, select, update, delete


BASE_DIR = os.path.dirname(__file__)
data = datetime.now().strftime('%H:%M %d/%m/%Y')

engine = sql.create_engine("sqlite://{BASE_DIR}/database_local.db")

Base = declarative.declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()