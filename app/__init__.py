from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api

from .config import Config
from .extensions import cors, db, migrate
from .routes import register_namespaces


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # JWT
    jwt = JWTManager(app)  # noqa: F841

    # API RESTX com versionamento
    api = Api(
        app,
        version="1.0",
        title="E-commerce API",
        description="API RESTful do sistema de e-commerce",
        prefix="/api/v1",
        doc="/docs",
    )

    # Registrar namespaces
    register_namespaces(api)

    return app
