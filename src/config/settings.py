# importing libraries
from flask_sqlalchemy import SQLAlchemy
from src import app

import sqlalchemy
from sqlalchemy import create_engine
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
#from sqlalchemy import inspect


# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:adMin#12@localhost:3306/encuestas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
engine=create_engine('mysql+mysqlconnector://root:adMin#12@localhost:3306/encuestas')
conn=engine.connect()
conn.execute("commit")