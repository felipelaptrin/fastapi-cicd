from fastapi.responses import JSONResponse
from api.schemas.response import FailureResponse, SuccessResponse

def default_response(func):
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)

        if isinstance(response, SuccessResponse):
            return JSONResponse(
                status_code=response.http_code,
                content={
                    "data": response.data
                }
            )
        elif isinstance(response, FailureResponse):
            return JSONResponse(
                status_code=response.http_code,
                content={
                    "error": {
                        "message": response.error_message
                    }
                }
            )
        else:
            raise Exception(
                f'Return type {type(response)} is not expected, only SuccessResponse and FailureResponse are valid.'
            )
    return inner
