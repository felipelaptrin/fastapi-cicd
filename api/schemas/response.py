from pydantic import BaseModel


class SuccessResponse(BaseModel):
    data: dict


class FailureResponse(BaseModel):
    error: str