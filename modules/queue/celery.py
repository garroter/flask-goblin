from celery import Celery
from app import create_app
import os


def make_celery(app):
    celery = Celery(
        app.import_name,
    )
    celery.conf.update(app.config["CELERY"])
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


app = create_app(os.environ.get("FLASK_CONFIG", "Dev"))
celery = make_celery(app)
