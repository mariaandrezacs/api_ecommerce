from .auth_routes import auth_bp
from .product_routes import product_bp
from .cart_routes import cart_bp
from .users_routes import user_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(user_bp)
