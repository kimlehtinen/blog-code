from src.modules.post.post import Post

class PostRepository:
    def find(self, id: int) -> "Post":
        raise NotImplementedError

    def add(self, post: Post) -> Post:
        raise NotImplementedError
