# importing libraries
from flask_sqlalchemy import SQLAlchemy
from src import app

import sqlalchemy
from sqlalchemy import create_engine
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
#from sqlalchemy import inspect


# Configure our Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:adMin#12@localhost:3306/encuestas'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://b9856c4e2b9364:cb17e2e2@us-cdbr-east-04.cleardb.com/heroku_f83b0e1ea8f66b4'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
#engine=create_engine('mysql+mysqlconnector://root:adMin#12@localhost:3306/encuestas')
engine=create_engine('mysql+mysqlconnector://b9856c4e2b9364:cb17e2e2@us-cdbr-east-04.cleardb.com/heroku_f83b0e1ea8f66b4')
conn=engine.connect()
conn.execute("commit")