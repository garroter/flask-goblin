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
     CELERY = {
        "broker_url": "pyamqp://***:***@****:5673",
        "include": ["modules.queue.tasks"],
        "task_ignore_result": True,
        "task_serializer": "json",
        "accept_content": ["application/json"],
        "result_serializer": "json",
        "celery_task_protocol": 1,
        "task_routes": {
            "modules.queue.tasks.run_queue": "name_rabbiqmq_queue"
        },
        "default_delay": 600, #in seconds
    }


class Test(Config):
    TESTING = True
