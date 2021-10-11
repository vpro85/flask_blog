import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SECRET_KEY = ')\x94/\x0b\x9f\xcd\xd6\xe9Cw2\x82\xbfS!\xbf\xc0\x86I\x02\xf0l\xf7\x9e'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')


class DevConfig(Config):
    debug = True
    SECRET_KEY = '\xe1Nb.\x08\xaf\x12x|\xe6#ua\xfem\xde\x0f\xcb~\xc9uA:\xda'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
