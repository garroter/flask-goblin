from flask import Flask
from extensions.database import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(f"config.config.{config}")
    db.init_app(app)
    from modules.example.views.example import ExampleView

    app.add_url_rule("/", view_func=ExampleView.as_view("Index"))
    return app
