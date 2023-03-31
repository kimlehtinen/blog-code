import pytest
from unittest.mock import MagicMock
from src.modules.post.post import Post
from src.modules.post.post_service import PostService


def test_get_single_post_details__returns_post_details_when_post_found():
    post = Post()
    post.id = 1
    post.title = "Mock Post"
    post.content = "This is a post"
    post.slug = "mock-post"
    mock_post_repository = MagicMock()
    mock_post_repository.find.return_value = post
    sut = PostService(post_repository=mock_post_repository)

    result = sut.get_single_post_details(id=post.id)

    assert result == {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "slug": post.slug
    }


def test_get_single_post_details__returns_None_when_no_post_found():
    mock_post_repository = MagicMock()
    mock_post_repository.find.return_value = None
    sut = PostService(post_repository=mock_post_repository)

    result = sut.get_single_post_details(id=5)

    assert result is None
    

