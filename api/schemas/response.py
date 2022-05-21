from pydantic import BaseModel


class SuccessResponse(BaseModel):
    http_code: int
    data: dict


class FailureResponse(BaseModel):
    http_code: int
    error_message: str