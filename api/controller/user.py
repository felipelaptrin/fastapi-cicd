from email import message
from api.repository.user import find_user_by_id
from api.schemas.response import FailureResponse, SuccessResponse
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
