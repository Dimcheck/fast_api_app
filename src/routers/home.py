from fastapi import APIRouter, Request

router = APIRouter(tags=["home"])


@router.get('/')
def home_page(request: Request):
    return {'data': 'home page'}
