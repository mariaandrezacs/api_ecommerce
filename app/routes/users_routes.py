from flask_login import login_required
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService


user_bp = Blueprint("user_bp", __name__, url_prefix="/api/users")


@user_bp.route("/", methods=["GET"])
@login_required
def list_users():
    users = UserService.list_users()
    return jsonify([{"id": u.id, "username": u.username} for u in users])


@user_bp.route("/create", methods=["POST"])

def create_user():
    data = request.json
    try:
        user = UserService.create_user(data["username"], data["password"])
        return jsonify({"id": user.id, "username": user.username})
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@user_bp.route("/delete/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    if UserService.delete_user(user_id):
        return jsonify({"message": "Usuário deletado"})
    return jsonify({"message": "Usuário não encontrado"}), 404
