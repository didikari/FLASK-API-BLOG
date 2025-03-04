import jwt
import datetime
from werkzeug.security import check_password_hash
from flask import current_app
from app.repositories.user_repository import UserRepository


class AuthService:
    @staticmethod
    def verify_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

    @staticmethod
    def login(email, password):
        user = UserRepository.get_user_by_email(email)
        if user and AuthService.verify_password(user.password_hash, password):
            exp_datetime = datetime.datetime.now(
                datetime.timezone.utc
            ) + datetime.timedelta(days=7)
            token = jwt.encode(
                {
                    "sub": str(user.id),
                    "exp": exp_datetime,
                },
                current_app.config["JWT_SECRET_KEY"],
                algorithm=current_app.config["JWT_ALGORITHM"],
            )
            return user, token
        return None, None
