from config import app, db
from models import *

def get_posts():
    return db.session.query(Post).all()

@app.route("/")
def index():
    posts = get_posts()
    
    html = ""

    if len(posts):
        for post in posts:
            html = html + f"<div><h1>{post.title}</h1><p>{post.content}</p><hr></div>"

    return html

if __name__ == '__main__':
    posts = get_posts()
    if not len(posts):
        new_post = Post(
            title="Example post",
            content="Hello world!",
            slug="example-post"
        )
        db.session.add(new_post)
        db.session.commit()
        print("Created post!")

    app.run(debug=True, host='0.0.0.0')
