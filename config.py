import os

class Config():

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://timothy:index506119056@localhost:5432/minutepitch'

    # SECRET_KEY = '08a505fc4b7dbb79a7bd93bccd526901'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://timothy:index506119056@localhost:5432/minutepitch'
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}
