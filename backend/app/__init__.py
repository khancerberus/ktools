from flask import Flask


def generate_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Development')

    return app
