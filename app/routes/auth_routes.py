from flask import Blueprint, jsonify, request
from flask_login import login_user, logout_user, login_required
from ..extensions import login_manager
from ..models.user import User
from ..services.user_service import UserService

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = UserService.find_by_username(data.get("username"))
    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message": "Logged in successfully"})
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})
