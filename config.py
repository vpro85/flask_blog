class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    pass


class DevConfig(Config):
    debug = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
