from flask import Flask, Blueprint, jsonify
from .extensions import db,cors
from .api.admin import admin
from .api.public import public


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    cors.init_app(app)

    app.register_blueprint(admin)
    app.register_blueprint(public)

    return app
