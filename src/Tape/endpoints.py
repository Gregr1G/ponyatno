from fastapi import APIRouter

router = APIRouter()

@router.get("/tape")
async def info_page():
    return {"hello": "world"}