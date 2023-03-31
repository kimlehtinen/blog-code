from src.modules.post.post_repository import PostRepository
from src.modules.post.post import Post

class PostService:
    _post_repository: PostRepository

    def __init__(self, post_repository: PostRepository) -> None:
        self._post_repository = post_repository

    def get_single_post_details(self, id: int) -> dict:
        post: Post = self._post_repository.find(id)

        if post:
            return post.to_dict()

        return None

    def create(self, post: Post) -> dict:
        post = self._post_repository.add(post)

        return post.to_dict()
