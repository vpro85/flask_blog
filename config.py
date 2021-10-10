class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SECRET_KEY = ')\x94/\x0b\x9f\xcd\xd6\xe9Cw2\x82\xbfS!\xbf\xc0\x86I\x02\xf0l\xf7\x9e'


class DevConfig(Config):
    debug = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = '\xe1Nb.\x08\xaf\x12x|\xe6#ua\xfem\xde\x0f\xcb~\xc9uA:\xda'
