from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

def create_app(configFileName):
    #creates flask application object
	flask_obj = Flask(__name__)	
	
	#set application database configeration
	objectName = 'config.' + configFileName
	flask_obj.config.from_object(objectName)
	
	#create database and map to the application	
	#db.init_app(flask_obj)
		
	return flask_obj
	

#app = create_app('Config')
app = create_app('Config')
#db = SQLAlchemy(app)
#db.create_all()

