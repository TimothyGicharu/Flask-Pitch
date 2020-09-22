import os

class Config():

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


    # SECRET_KEY = '08a505fc4b7dbb79a7bd93bccd526901'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://timothy:index506119056@localhost/minutepitch'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}
