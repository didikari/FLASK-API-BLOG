from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, JWTManager
from app.repositories.user_repository import UserRepository
from werkzeug.exceptions import Unauthorized


def jwt_required_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            # Verifikasi token JWT di request
            verify_jwt_in_request()

            # Ambil user_id dari token
            user_id = get_jwt_identity()

            # Ambil data user berdasarkan user_id
            user = UserRepository.get_by_id(user_id)

            if not user:
                return jsonify({"message": "User not found"}), 404

            # Lanjutkan dengan user yang sudah terverifikasi
            return func(user, *args, **kwargs)
        except Unauthorized:
            return jsonify({"message": "Token is missing or invalid"}), 401
        except Exception as e:
            return jsonify({"message": str(e)}), 500

    return decorated_function
