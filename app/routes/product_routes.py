from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.services.product_service import ProductService

ns_product = Namespace("products", description="Gerenciamento de produtos")

product_model = ns_product.model(
    "Product",
    {
        "name": fields.String(required=True),
        "price": fields.Float(required=True),
        # "stock": fields.Integer(required=True),
    },
)


@ns_product.route("/")
class ProductList(Resource):
    @jwt_required()
    def get(self):
        """Lista todos os produtos"""
        return ProductService.list_all()

    @ns_product.expect(product_model)
    @jwt_required()
    def post(self):
        """Cria um novo produto"""
        data = ns_product.payload
        return ProductService.add(data)


@ns_product.route("/<int:id>")
class ProductDetail(Resource):
    @jwt_required()
    def get(self, id):
        """Obtém um produto"""
        product = ProductService.get_by_id(id)
        if not product:
            ns_product.abort(404, "Product not found")
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
        }

    @ns_product.expect(product_model)
    @jwt_required()
    def put(self, id):
        """Atualiza produto existente"""
        product = ProductService.get_by_id(id)
        if not product:
            ns_product.abort(404, "Product not found")
        data = ns_product.payload
        return ProductService.update(product, data)

    @jwt_required()
    def delete(self, id):
        """Deleta um produto"""
        product = ProductService.get_by_id(id)
        if not product:
            ns_product.abort(404, "Product not found")
        return ProductService.delete(product)


@ns_product.route("/<int:product_id>")
class ProductUpdate(Resource):
    @ns_product.expect(product_model)
    def put(self, product_id):
        """Atualiza um produto existente"""
        product = ProductService.get_by_id(product_id)
        if not product:
            ns_product.abort(404, "Product not found")
        data = ns_product.payload
        return ProductService.update(product, data)


@ns_product.route("/<int:product_id>")
class ProductDelete(Resource):
    def delete(self, product_id):
        product = ProductService.get_by_id(product_id)
        if not product:
            ns_product.abort(404, "Product not found")
        return ProductService.delete(product)
