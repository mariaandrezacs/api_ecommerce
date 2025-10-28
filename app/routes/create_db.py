from flask_restx import Namespace, Resource

from app.extensions import db

ns_create = Namespace("createdb", description="Criar o banco de dados")


@ns_create.route("/")
class CreateDB(Resource):
    def post(self):
        """
        Cria todas as tabelas do banco de dados.
        """
        try:
            db.create_all()
            return {"status": "Database created"}, 201
        except Exception as e:
            return {"status": "Error creating database", "error": str(e)}, 500
