from ..models.cart_item import CartItem
from ..models.product import Product
from ..extensions import db

class CartService:
    @staticmethod
    def add_item(user, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return {"message": "Item added to the cart successfully"}

    @staticmethod
    def remove_item(user, product_id):
        cart_item = CartItem.query.filter_by(
            user_id=user.id, product_id=product_id
        ).first()
        if not cart_item:
            return {"message": "Item not in cart"}, 404
        db.session.delete(cart_item)
        db.session.commit()
        return {"message": "Item removed successfully"}

    @staticmethod
    def view_cart(user):
        items = CartItem.query.filter_by(user_id=user.id).all()
        cart_content = []
        for item in items:
            cart_content.append({
                "id": item.id,
                "product_id": item.product_id,
                "user_id": item.user_id
            })
        return cart_content

    @staticmethod
    def checkout(user):
        items = CartItem.query.filter_by(user_id=user.id).all()
        for item in items:
            db.session.delete(item)
        db.session.commit()
        return {"message": "Checkout complete. Cart cleared."}
