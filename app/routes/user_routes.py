from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import jwt_required_middleware
from app.services.user_service import UserService

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = UserService.register(data["username"], data["email"], data["password"])
    return (
        jsonify({"message": "User registered successfully", "user": user.username}),
        201,
    )


@user_bp.route("/", methods=["GET"])
@jwt_required_middleware
def get_all_user(user):
    users = UserService.get_all_user()
    return (
        jsonify(
            {
                "message": "Get all user successfully!",
                "users": [
                    {"id": user.id, "username": user.username, "email": user.email}
                    for user in users
                ],
            }
        ),
        200,
    )


@user_bp.route("/profile", methods=["GET"])
@jwt_required_middleware
def profile(user):
    return (
        jsonify(
            {
                "message": "Get user profile successfully!",
                "user": {"id": user.id, "username": user.username, "email": user.email},
            }
        ),
        200,
    )
