from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from ..services.cart_service import CartService

cart_bp = Blueprint("cart_bp", __name__, url_prefix="/api/cart")

@cart_bp.route("/", methods=["GET"])
@login_required
def view_cart():
    return jsonify(CartService.view_cart(current_user))

@cart_bp.route("/add/<int:product_id>", methods=["POST"])
@login_required
def add_item(product_id):
    return jsonify(CartService.add_item(current_user, product_id))

@cart_bp.route("/remove/<int:product_id>", methods=["DELETE"])
@login_required
def remove_item(product_id):
    return jsonify(CartService.remove_item(current_user, product_id))

@cart_bp.route("/checkout", methods=["POST"])
@login_required
def checkout():
    return jsonify(CartService.checkout(current_user))
