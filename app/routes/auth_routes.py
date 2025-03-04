from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user, token = AuthService.login(data["email"], data["password"])

    if user:
        return (
            jsonify(
                {"message": "Login successful", "user": user.username, "token": token}
            ),
            200,
        )
    else:
        return jsonify({"message": "Invalid credentials"}), 401
