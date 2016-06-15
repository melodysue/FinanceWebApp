import os
# default config

'''
environment variable needs to be set each time.
Run following command on mac:
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/financewebapp_dev"
Run following command on Windows:
SET (...)
'''
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "xac\xa3\x9b;\x10\x96\xaf\x90\x85\x9e\x15\xc15\x92A\x12"
	SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
	print SQLALCHEMY_DATABASE_URI

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False