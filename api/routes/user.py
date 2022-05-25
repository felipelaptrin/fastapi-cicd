from api.controller.user import get_user, create_user, delete_user, put_user
from api.schemas.user import UserInfo

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=['User'])


@router.get("/{user_id}")
def get(user_id: int):
    response = get_user(user_id)
    return response


@router.post("")
def post(user: UserInfo):
    response = create_user(user)
    return response


@router.delete("/{user_id}")
def delete(user_id: int):
    response = delete_user(user_id)
    return response


@router.put("/{user_id}")
def put(user_id: int, user: UserInfo):
    response = put_user(user_id, user)
    return response