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

    @staticmethod
    def find_by_username(username: str) -> User | None:
        """Busca um usuário pelo username"""
        return User.query.filter_by(username=username).first()

    @staticmethod
    def list_users() -> list[User]:
        return User.query.all()

    @staticmethod
    def delete_user(user_id: int) -> bool:
        user = User.query.get(user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True

    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        return User.query.get(user_id)
