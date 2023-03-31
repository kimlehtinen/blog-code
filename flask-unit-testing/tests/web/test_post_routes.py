import pytest
from unittest.mock import MagicMock
from src.modules.post.post import Post


def test_get_single_post__returns_post_details_when_found(client, app):
    post = Post()
    post.id = 1
    post.title = "Mock Post"
    post.content = "This is a post"
    post.slug = "mock-post"
    mock_post_repository = MagicMock()
    mock_post_repository.find.return_value = post
    app.container.post_repository.override(mock_post_repository)

    response = client.get("/post/1")

    assert response.status_code == 200
    assert response.json == {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "slug": post.slug
    }


def test_get_single_post__returns_not_found_when_post_details_not_found(client, app):
    mock_post_repository = MagicMock()
    mock_post_repository.find.return_value = None
    app.container.post_repository.override(mock_post_repository)

    response = client.get("/post/1")

    assert response.status_code == 404
    assert response.json == {"message": "Unable to find post 1"}
