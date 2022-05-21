from api.controller.user import get_user
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=['User'])


@router.get("/{user_id}")
def get(user_id: int):
    user = get_user(user_id)
    return user
