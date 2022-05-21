from email import message
import logging

from api.repository.user import find_user_by_id
from api.schemas.response import FailureResponse, SuccessResponse


def get_user(user_id: int):
    try:
        user = find_user_by_id(user_id)
        return SuccessResponse(
            data=user.__data__
        )
    except Exception as e:
        print(e)
        return FailureResponse(
            error="Something went wrong while trying to get the info from the database."
        )
