import os


# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x811[rE\x9f\xe3>i\xac\xbf\xe7\xfd\x13/j\xec@\xae\x1eS\tT\x00'
	SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
	#SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False


