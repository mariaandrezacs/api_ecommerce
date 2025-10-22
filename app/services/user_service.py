from app.extensions import db
from app.models.user import User

class UserService:

    @staticmethod
    def create_user(username: str, password: str) -> User:
        if User.query.filter_by(username=username).first():
            raise ValueError("Usuário já existe")
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user
