import pytest
from flask import g
import sqlite3
from factory import create_app
from app.db_queries import *
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#from config import SQLALCHEMY_DATABASE_URI
import config


@pytest.fixture(scope = 'session')
def application():	
	app_obj = create_app('TestConfig')
	#app_obj.config.from_object('config.TestConfig')
	
	#db.create_all()
	#g.db = sqlite3.connect(app_obj.config['SQLALCHEMY_DATABASE_URI'])
	return app_obj
	
test_app = application()	
from app.models import db


#@pytest.fixture(scope = 'session')
#def teardown_request(db_setup):
#	g.db.close()
        
        	   
    
	
	
	
