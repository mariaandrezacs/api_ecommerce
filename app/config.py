import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "@senha123")  # fallback para dev
    SQLALCHEMY_DATABASE_URI = "sqlite:///ecommerce.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
