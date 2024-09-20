from database import async_session_maker as async_session
from src.Post.schemas import PostSchema
from src.Post.models import Post
from sqlalchemy import select
# import asyncio

class PostRepository:
    @classmethod
    async def create_post(cls, post: PostSchema):
        async with async_session() as session:
            session.add(post)
            await session.commit()
        return post

    @classmethod
    async def delete_post(cls):
        pass

    @classmethod
    async def update_post(cls):
        pass

    @classmethod
    async def get_posts(cls):
        pass
