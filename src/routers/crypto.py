from typing import List

from auth.auth import oauth2_scheme
from database.dependencies import get_db
from fastapi import APIRouter, Depends, Response, status
from fastapi.exceptions import HTTPException
from models.crypto import Crypto
from schemas.items import CryptoSchema
from sqlalchemy.orm import Session
from utils.crud import get_crypto, post_crypto

router = APIRouter(tags=["crypto"])


@router.get('/crypto/', dependencies=[Depends(oauth2_scheme)], response_model=List[CryptoSchema])
def read_crypto(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_crypto(db, skip=skip, limit=limit)
    return items


@router.post('/crypto/', dependencies=[Depends(oauth2_scheme)], response_model=CryptoSchema)
def create_crypto(crypto: CryptoSchema, db: Session = Depends(get_db)) -> Crypto:
    return post_crypto(db=db, crypto=crypto)
