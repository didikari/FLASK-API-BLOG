from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, JWTManager
from app.repositories.user_repository import UserRepository
from werkzeug.exceptions import Unauthorized


def jwt_required_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            verify_jwt_in_request()

            user_id = get_jwt_identity()

            user = UserRepository.get_by_id(user_id)

            if not user:
                return jsonify({"message": "User not found"}), 404

            return func(user, *args, **kwargs)
        except Unauthorized:
            return jsonify({"message": "Token is missing or invalid"}), 401
        except Exception as e:
            return jsonify({"message": str(e)}), 500

    return decorated_function
