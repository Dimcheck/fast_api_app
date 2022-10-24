from models.items import Item
from models.crypto import Crypto
from schemas.items import ItemSchema, CryptoSchema
from sqlalchemy.orm import Session


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_crypto(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Crypto).offset(skip).limit(limit).all()


def post_item(item: ItemSchema, db: Session) -> ItemSchema:
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def post_crypto(crypto: CryptoSchema, db: Session) -> CryptoSchema:
    db_crypto = Crypto(**crypto.dict())
    db.add(db_crypto)
    db.commit()
    db.refresh(db_crypto)
    return db_crypto
