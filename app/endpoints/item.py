from fastapi import APIRouter, HTTPException
from app.models.item import ItemModel
from app.db.database import database
from bson import ObjectId

router = APIRouter()

@router.post("/items/", response_model=ItemModel)
async def create_item(item: ItemModel):
    new_item = await database["items"].insert_one(item.dict(by_alias=True))
    created_item = await database["items"].find_one({"_id": new_item.inserted_id})
    return created_item

@router.get("/items/{item_id}", response_model=ItemModel)
async def read_item(item_id: str):
    if (item := await database["items"].find_one({"_id": ObjectId(item_id)})) is not None:
        return item
    raise HTTPException(status_code=404, detail="Item not found")