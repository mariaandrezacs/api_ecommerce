from flask_login import UserMixin

from ..extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"  # Evita palavra reservada
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    # Relacionamento com CartItem
    cart_items = db.relationship("CartItem", back_populates="user")
