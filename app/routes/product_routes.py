from flask import Blueprint, jsonify, request
from flask_login import login_required
from ..models.product import Product
from ..services.product_service import ProductService

product_bp = Blueprint("product_bp", __name__, url_prefix="/api/products")

@product_bp.route("/", methods=["GET"])
def list_products():
    return jsonify(ProductService.list_all())

@product_bp.route("/add", methods=["POST"])
@login_required
def add_product():
    data = request.json
    return jsonify(ProductService.add(data))

@product_bp.route("/update/<int:product_id>", methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    data = request.json
    return jsonify(ProductService.update(product, data))

@product_bp.route("/delete/<int:product_id>", methods=["DELETE"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(ProductService.delete(product))
