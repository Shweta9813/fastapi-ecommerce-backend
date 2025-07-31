from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="abcd@gmail.com")
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        example="strongpassword123",
        description="Password must be at least 8 characters long.",
    )

    model_config = ConfigDict(
        title="UserLogin",
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {
                "email":"abc@gmail.com",
                "password": "strongpassword123",
            }   
        },
    )

class UserLoginResponse(BaseModel):
        message: str
        token: str
        
