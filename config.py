import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'babtdaddy67@gmail.com'
    MAIL_PASSWORD = '8Mo9un20se17y'

    SECRET_KEY = 'S3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://postgres:mulama@127.0.0.1:5432/lawdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_PASSWORD = 'P@ssw0rd!'


    DEBUG = False
    TESTING = False
    FLASK_DEBUG = 0

class Development(Config):
    DEVELOPMENT = True
    DEBUG = True

class Production(Config):
    DEBUG = False

class Testing(Config):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    CSRF_ENABLED = False
    LOGIN_DISABLED = True
    WTF_CSRF_ENABLED = False


config = {
    'development': 'app.config.DevelopmentConfig',
    'testing': 'app.config.TestingConfig',
    'default': 'app.config.ProductionConfig'
}