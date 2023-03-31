from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from src.di.di_container import DI
from src.modules.post.post_service import PostService
from src.modules.post.post import Post


post_api = Blueprint("post_api", __name__)


@post_api.route("/<id>", methods=["GET"])
@inject
def get_single_post(id: str, post_service: PostService = Provide[DI.post_service]):
    post_details: dict = post_service.get_single_post_details(int(id))

    if not post_details:
        return jsonify({"message": f"Unable to find post {str(id)}"}), 404

    return jsonify(post_details), 200


@post_api.route("/", methods=["POST"])
@inject
def create_post(post_service: PostService = Provide[DI.post_service]):
    post_data = request.get_json()
    post = Post()
    post.title = post_data["title"]
    post.content = post_data["content"]
    post.slug = post_data["slug"]

    post_details: dict = post_service.create(post)

    return jsonify(post_details), 201
