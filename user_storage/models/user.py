from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    user_name: str = Field(description="User name")
    first_name: str = Field(description="First Name")
    last_name: str = Field(description="Last Name")
    email: EmailStr = Field(description="Email")
    phone: str = Field(description="Phone")


class UserResponse(User):
    user_id: int = Field(description="User ID")