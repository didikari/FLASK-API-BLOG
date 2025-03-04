from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import jwt_required_middleware
from app.services.post_service import PostService
from app.helpers.api_response import ApiResponse

post_bp = Blueprint("post", __name__)


@post_bp.route("/store", methods=["POST"])
@jwt_required_middleware
def create(user):
    data = request.get_json()

    if "title" not in data or "content" not in data:
        return jsonify({"message": "Title and content are required"}), 400

    post = PostService.create(data["title"], data["content"], user.id)

    return ApiResponse.format(
        {"post": {"title": post.title, "content": post.content}},
        201,
        "Post created successfully",
    )


@post_bp.route("/", methods=["GET"])
@jwt_required_middleware
def get_all(user):
    posts = PostService.get_all()
    post_data = [
        {"id": post.id, "title": post.title, "content": post.content} for post in posts
    ]

    return ApiResponse.format({"posts": post_data}, 200, "Get all posts successfully")


@post_bp.route("/<int:id>", methods=["GET"])
@jwt_required_middleware
def get_by_id(user, id):
    post = PostService.get_by_id(id)

    if not post:
        return ApiResponse.format({}, 404, "Post not found")

    return ApiResponse.format(
        {"id": post.id, "title": post.title, "content": post.content},
        200,
        "Get post by id successfully",
    )


@post_bp.route("/<int:id>", methods=["PUT"])
@jwt_required_middleware
def update(user, id):
    data = request.get_json()

    if "title" not in data or "content" not in data:
        return ApiResponse.format({}, 400, "Title and content are required")

    post = PostService.update(id, data["title"], data["content"])

    return ApiResponse.format(
        {"post": {"title": post.title, "content": post.content}},
        200,
        "Post updated successfully",
    )


@post_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required_middleware
def delete(user, id):
    post = PostService.delete(id)

    return ApiResponse.format(
        {"post": {"title": post.title, "content": post.content}},
        200,
        "Post deleted successfully",
    )
