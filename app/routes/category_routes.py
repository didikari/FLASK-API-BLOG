from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import jwt_required_middleware
from app.services.category_service import CategoryService
from app.helpers.api_response import ApiResponse

category_bp = Blueprint("category", __name__)


@category_bp.route("/store", methods=["POST"])
@jwt_required_middleware
def create(
    user,
):
    data = request.get_json()

    if "name" not in data:
        return jsonify({"message": "Category name is required"}), 400

    category = CategoryService.create(data["name"])

    return ApiResponse.format(
        {"category": category.name}, 201, "Category created successfully"
    )


@category_bp.route("/", methods=["GET"])
@jwt_required_middleware
def get_all(user):
    categories = CategoryService.get_all()
    category_data = [
        {"id": category.id, "name": category.name} for category in categories
    ]

    return ApiResponse.format(
        {"categories": category_data}, 200, "Get all categories successfully"
    )


@category_bp.route("/<int:id>", methods=["GET"])
@jwt_required_middleware
def get_by_id(user, id):
    category = CategoryService.get_by_id(id)

    if not category:
        return ApiResponse.format({}, 404, "Category not found")

    return ApiResponse.format(
        {"id": category.id, "name": category.name},
        200,
        "Get category by id successfully",
    )


@category_bp.route("/<int:id>", methods=["PUT"])
@jwt_required_middleware
def update(user, id):
    data = request.get_json()

    if "name" not in data:
        return ApiResponse.format({}, 400, "Category name is required")

    category = CategoryService.update(id, data["name"])

    return ApiResponse.format(
        {"id": category.id, "name": category.name}, 200, "Category updated successfully"
    )


@category_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required_middleware
def delete(user, id):
    category = CategoryService.delete(id)

    return ApiResponse.format(
        {"id": category.id, "name": category.name}, 200, "Category deleted successfully"
    )
