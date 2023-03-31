class Post:
    id: int
    title: str
    content: str
    slug: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "slug": self.slug
        }
