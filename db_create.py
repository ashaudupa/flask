#!flask/bin/python
from migrate.versioning import api
#from config import BaseConfigeration
from app.models import db
from config import Config
import os.path
db.create_all()
print "db tables created"
if not os.path.exists(Config.SQLALCHEMY_MIGRATE_REPO):
	api.create(Config.SQLALCHEMY_MIGRATE_REPO,'data_repository')
	api.version_control(Config.SQLALCHEMY_DATABASE_URI,Config.SQLALCHEMY_MIGRATE_REPO)
else:
	api.version_control(Config.SQLALCHEMY_DATABASE_URI,Config.SQLALCHEMY_MIGRATE_REPO,api.version(Config.SQLALCHEMY_MIGRATE_REPO))
