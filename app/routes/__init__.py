from .auth_routes import ns_auth
from .cart_routes import ns_cart
from .create_db import ns_create
from .product_routes import ns_product
from .users_routes import ns_user


def register_namespaces(api):
    api.add_namespace(ns_auth, path="/auth")
    api.add_namespace(ns_user, path="/users")
    api.add_namespace(ns_product, path="/products")
    api.add_namespace(ns_cart, path="/cart")
    api.add_namespace(ns_create, path="/createdb")
