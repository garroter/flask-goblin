class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite://:memory:"


class Prod(Config):
    DEBUG = False
    TESTING = False


class Dev(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://username:password@host:3306/database"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ECHO = False


class Test(Config):
    TESTING = True
