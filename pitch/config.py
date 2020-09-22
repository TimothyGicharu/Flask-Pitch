import os

class Config():
    SECRET_KEY = '08a505fc4b7dbb79a7bd93bccd526901'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://timothy:index506119056@localhost/minutepitch'


class DevConfig():
    pass

class ProdConfig():
    pass
