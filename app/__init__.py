from flask import Flask
from flasgger import Swagger
from .extensions import db, login_manager, cors
from .config import Config
from .routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)
    login_manager.login_view = "auth_bp.login"

    register_blueprints(app)

    Swagger(app)

    return app
