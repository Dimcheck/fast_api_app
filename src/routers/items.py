from fastapi import APIRouter, Depends
from models.items import Item
from schemas.items import ItemSchema
from sqlalchemy.orm import Session
from database.dependencies import get_db
from utils.crud import get_items, post_item


router = APIRouter(tags=["items"])


@router.get('/items/', response_model=list[ItemSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items


@router.post('/items/', response_model=ItemSchema)
def create_items(item: ItemSchema, db: Session = Depends(get_db)) -> Item:
    return post_item(db=db, item=item)
