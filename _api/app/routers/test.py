from fastapi import APIRouter
from fastapi.responses import RedirectResponse
router = APIRouter()

@router.get("/api/test")
async def read_items():
    return {"test": ["Foo", "Bar"]}