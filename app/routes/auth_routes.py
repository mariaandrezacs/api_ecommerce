from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.user_service import UserService

ns_auth = Namespace("auth", description="Autenticação de usuários")

login_model = ns_auth.model(
    "Login",
    {
        "username": fields.String(required=True, description="Nome de usuário"),
        "password": fields.String(required=True, description="Senha"),
    },
)


@ns_auth.route("/")
class Login(Resource):
    def post(self):
        data = ns_auth.payload
        user = UserService.find_by_username(data.get("username"))
        if user and data.get("password") == user.password:
            access_token = create_access_token(identity=str(user.id))
            return {"access_token": access_token}
        ns_auth.abort(401, "Invalid credentials")


@ns_auth.route("/")
class Profile(Resource):
    @jwt_required()
    def get(self):
        """Retorna os dados do usuário autenticado"""
        user_id = get_jwt_identity()
        user = UserService.get_by_id(user_id)
        return {"id": user.id, "username": user.username}
