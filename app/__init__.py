from flask import Flask
from app.views import server_bp
from settings import APP_SETTINGS


def create_app(settings=None):
    app = Flask(__name__)

    if settings:
        app.config.from_object(settings)
    else:
        app_settings = APP_SETTINGS
        app.config.from_object(app_settings)

    app.register_blueprint(server_bp)

    return app
