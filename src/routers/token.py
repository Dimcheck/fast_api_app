from auth.auth import create_access_token
from fastapi import APIRouter

router = APIRouter(tags=["token"])


@router.get('/get_token')
def home_page():
    return create_access_token({'data': 'value'})
