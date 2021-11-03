from flask_sqlalchemy import SQLAlchemy
from rflask import app
from sqlalchemy.sql import select 
from sqlalchemy import create_engine

db = SQLAlchemy(app)
engine = create_engine('sqlite:///:memory:', echo=True)
