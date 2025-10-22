from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService

# Criar Namespace
ns_user = Namespace("users", description="Gerenciamento de usuários")

# Modelo de dados para documentação automática
user_model = ns_user.model(
    "User",
    {
        "username": fields.String(required=True, description="Nome de usuário"),
        "password": fields.String(required=True, description="Senha do usuário"),
    },
)


# Endpoint para listar usuários
@ns_user.route("/")
class UserList(Resource):
    def get(self):
        """Lista todos os usuários"""
        users = UserService.list_users()
        return [{"id": u.id, "username": u.username} for u in users]


# Endpoint para criar usuário
@ns_user.route("/create")
class UserCreate(Resource):
    @ns_user.expect(user_model)
    def post(self):
        """Cria um novo usuário"""
        data = ns_user.payload
        try:
            user = UserService.create_user(data["username"], data["password"])
            return {"id": user.id, "username": user.username}
        except ValueError as e:
            ns_user.abort(400, str(e))


# Endpoint para deletar usuário
@ns_user.route("/delete/<int:user_id>")
class UserDelete(Resource):
    def delete(self, user_id):
        """Deleta um usuário pelo ID"""
        if UserService.delete_user(user_id):
            return {"message": "Usuário deletado"}
        ns_user.abort(404, "Usuário não encontrado")
