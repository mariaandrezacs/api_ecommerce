from flask_restx import Namespace, Resource

from app.extensions import db

ns_create = Namespace("createdb", description="Criar o banco de dados")


@ns_create.route("/")
class CreateDB(Resource):
    def get(self):
        db.create_all()
        return {"status": "Database created"}
