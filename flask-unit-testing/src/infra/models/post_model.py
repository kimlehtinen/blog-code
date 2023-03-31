from db import db
from src.modules.post.post import Post

class PostModel(db.Model, Post):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text())
    slug = db.Column(db.String(50))
