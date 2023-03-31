from dependency_injector import containers, providers
from src.infra.repositories.post_repository_impl import PostRepositoryImpl
from src.modules.post.post_service import PostService


class DI(containers.DeclarativeContainer):
    post_repository = providers.Factory(PostRepositoryImpl)
    post_service = providers.Factory(PostService, post_repository=post_repository)
