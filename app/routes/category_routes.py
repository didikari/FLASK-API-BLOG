from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import jwt_required_middleware
from app.services.category_service import CategoryService

category_bp = Blueprint("category", __name__)


@category_bp.route("/store", methods=["POST"])
@jwt_required_middleware  # Pastikan hanya pengguna yang sudah login yang dapat mengakses
def create(
    user,
):
    data = request.get_json()

    # Validasi nama kategori
    if "name" not in data:
        return jsonify({"message": "Category name is required"}), 400

    # Panggil service untuk membuat kategori
    category = CategoryService.create(data["name"])

    return (
        jsonify(
            {"message": "Category created successfully", "category": category.name}
        ),
        201,
    )
