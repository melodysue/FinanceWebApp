import os
# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "xac\xa3\x9b;\x10\x96\xaf\x90\x85\x9e\x15\xc15\x92A\x12"
	SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
	print SQLALCHEMY_DATABASE_URI

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False