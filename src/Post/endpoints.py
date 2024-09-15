from fastapi import APIRouter

post_router = APIRouter()


@post_router.get("/get_posts")
async def tape_page():
    return {"hello": "world"}


@post_router.get("/{post_id}")
async def tape_page():
    return {"hello": "world"}


@post_router.post("/create")
async def create_post():
    return {"hello": "world"}


@post_router.delete("/delete")
async def create_post():
    return {"hello": "world"}
