from werkzeug.security import generate_password_hash
from app.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def register(username, email, password):
        hashed_password = generate_password_hash(password)
        return UserRepository.create_user(username, email, hashed_password)

    @staticmethod
    def get_all_user():
        return UserRepository.get_all_user()
