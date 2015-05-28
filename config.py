import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(basedir,'app.db')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
	WTF_CSRF_ENABLED = True
	SECRET_KEY='you-will-never-guess'
	TESTING = False

class TestConfig(Config):
   TESTING =True
#   WTF_CSRF_ENABLED = True
#   SECRET_KEY = 'you-will-never-guess'
   SQLALCHEMY_DATABASE_URI ='sqlite:///'+os.path.join(basedir,'test.db')
   SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'test_db_repository')

