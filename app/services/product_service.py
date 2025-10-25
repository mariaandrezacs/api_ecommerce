from ..extensions import db
from ..models.product import Product


class ProductService:
    @staticmethod
    def list_all():
        products = Product.query.all()
        return [{"id": p.id, "name": p.name, "price": p.price} for p in products]

    @staticmethod
    def get_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def add(data):
        if "name" not in data or "price" not in data:
            return {"message": "Invalid product data"}, 400

        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", ""),
        )
        db.session.add(product)
        db.session.commit()
        return {"message": "Product added successfully"}

    @staticmethod
    def update(product, data):
        if "name" in data:
            product.name = data["name"]
        if "price" in data:
            product.price = data["price"]
        if "description" in data:
            product.description = data["description"]
        db.session.commit()
        return {"message": "Product updated successfully"}

    @staticmethod
    def delete(product):
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted successfully"}
