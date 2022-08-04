from models.items import Item
from schemas.items import ItemSchema
from sqlalchemy.orm import Session


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def post_item(item: ItemSchema, db: Session) -> ItemSchema:
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
