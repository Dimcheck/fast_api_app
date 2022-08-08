from typing import List

from auth.auth import oauth2_scheme
from database.dependencies import get_db
from fastapi import APIRouter, Depends, Response, status
from fastapi.exceptions import HTTPException
from models.items import Item
from schemas.items import ItemSchema
from sqlalchemy.orm import Session
from utils.crud import get_items, post_item

router = APIRouter(tags=["items"])


@router.get('/items/', dependencies=[Depends(oauth2_scheme)], response_model=List[ItemSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items


@router.post('/items/', dependencies=[Depends(oauth2_scheme)], response_model=ItemSchema)
def create_items(resp: Response, item: ItemSchema, db: Session = Depends(get_db)) -> Item:
    if item.is_broken is True:
        resp.status_code = status.HTTP_418_IM_A_TEAPOT
        raise HTTPException(detail='fix the item before posting it ;)', status_code=status.HTTP_418_IM_A_TEAPOT)
    return post_item(db=db, item=item)
