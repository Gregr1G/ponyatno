from fastapi import APIRouter

router_info = APIRouter()

@router_info.get("/info")
async def info_page():
    return {"info": "info"}