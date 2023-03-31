from src.modules.post.post_repository import PostRepository
from src.modules.post.post import Post
from src.infra.models.post_model import PostModel
from db import db


class PostRepositoryImpl(PostRepository):
    def find(self, id: int) -> "Post":
        return db.session.query(PostModel).filter_by(id=id).first()

    def add(self, post: Post) -> Post:
        post_db = PostModel()
        post_db.title = post.title
        post_db.content = post.content
        post_db.slug = post.slug
        
        db.session.add(post_db)
        db.session.commit()

        return post_db
