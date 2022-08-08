from auth.auth import oauth2_scheme
from fastapi import APIRouter, Depends

router = APIRouter(tags=["home"])


@router.get('/', dependencies=[Depends(oauth2_scheme)])
def home_page():
    return {'data': 'authenticated data'}
