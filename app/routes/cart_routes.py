from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.cart_service import CartService

ns_cart = Namespace("cart", description="Gerenciamento do carrinho")

@ns_cart.route("/")
class Cart(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        return CartService.view_cart(user_id)

@ns_cart.route("/<int:product_id>")
class AddToCart(Resource):
    @jwt_required()
    def post(self, product_id):
        user_id = get_jwt_identity()
        return CartService.add_item(user_id, product_id)

@ns_cart.route("/<int:product_id>")
class RemoveFromCart(Resource):
    @jwt_required()
    def delete(self, product_id):
        user_id = get_jwt_identity()
        return CartService.remove_item(user_id, product_id)

@ns_cart.route("/checkout")
class Checkout(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        return CartService.checkout(user_id)
