from turtle import ht
from api.repository.user import (
    add_user, find_user_by_id, delete_user_by_id, update_user_by_id
)
from api.schemas.response import FailureResponse, SuccessResponse
from api.schemas.user import UserInfo
from api.utils.response import default_response

@default_response
def get_user(user_id: int):
    try:
        user = find_user_by_id(user_id)
        if user:
            return SuccessResponse(
                http_code=200,
                data=user.__data__
            )
        else:
            return FailureResponse(
                http_code=404,
                error_message=f"User with id {user_id} was not found."
            )
    except Exception as e:
        print(e)
        return FailureResponse(
            http_code=500,
            error_message="Something went wrong while trying to get the info from the database."
        )


@default_response
def create_user(user: UserInfo):
    try:
        added_user = add_user(user)
        return SuccessResponse(
            http_code=201,
            data=added_user.__data__
        )
    except Exception as e:
        print(e)
        return FailureResponse(
            http_code=500,
            error_message="Something went wrong while trying to insert the user in the database."
        )


@default_response
def delete_user(user_id: int):
    try:
        deleted_user = delete_user_by_id(user_id)
        return SuccessResponse(
            http_code=200,
            data=deleted_user.__data__
        )
    except Exception as e:
        print(e)
        return FailureResponse(
            http_code=500,
            error_message="Given user ID does not exist."
        )


@default_response
def put_user(user_id: int, user: UserInfo):
    try:
        user_exists = True if get_user(user_id).status_code == 200 else False
        if user_exists:
            update_user_by_id(user_id, user)
        return SuccessResponse(
            http_code=200,
            data=dict(user)
        )
    except Exception as e:
        print(e)
        return FailureResponse(
            http_code=500,
            error_message="Something went wrong while trying to insert the user in the database."
        )