from fastapi import APIRouter
from app.api.endpoints import items

router = APIRouter()
router.include_router(items.router, tags=["items"])