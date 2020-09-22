import os

class Config():

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://nzvxtbraakpbzr:0ded620ec8db233868c78c4bf5ea352da37b4e0376bc6a964e29f9bdeb002ae0@ec2-52-207-124-89.compute-1.amazonaws.com:5432/d6riaoth9obntg'

    # SECRET_KEY = '08a505fc4b7dbb79a7bd93bccd526901'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://timothy:index506119056@localhost:5432/minutepitch'
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}
