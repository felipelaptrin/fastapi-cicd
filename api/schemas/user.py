from pydantic import BaseModel, Field, EmailStr


class UserInfo(BaseModel):
    first_name: str = Field(..., description="First name of the user")
    last_name: str = Field(..., description="Last name of the user")
    email: EmailStr = Field(None, description="Main email of the user")
    is_active: bool = Field(..., description="Flag to indicate if user is active")