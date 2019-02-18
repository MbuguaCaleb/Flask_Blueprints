from flask import Flask, Blueprint
from .api.v1 import version1 as v1


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes=False
    app.register_blueprint(v1)

    return app







