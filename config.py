import os
# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "real_secret_key_hidden"
	db_string = os.environ["DATABASE_URL"]
	SQLALCHEMY_DATABASE_URI = db_string

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False