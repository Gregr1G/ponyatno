from fastapi import APIRouter

router = APIRouter()

@router.get("/tape")
async def tape_page():
    return {"hello": "world"}
