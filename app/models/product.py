from ..extensions import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relacionamento com CartItem
    cart_items = db.relationship("CartItem", back_populates="product")
