from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import Optional
from bson import ObjectId

<<<<<<< HEAD
class UserRegistration(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        example="John Doe"
    )
    username: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        example="john_doe"
    )
    email: EmailStr = Field(
        ...,
        example="john.doe@example.com"
    )
    phone_number: str = Field(
        ...,
        min_length=10,
        max_length=15,
        example="+1234567890"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=128, 
        example="strongpassword123",
        description="Password must be at least 8 characters long."
=======

class UserRegistration(BaseModel):

    id: Optional[str] = Field(
        default_factory=lambda: str(ObjectId()),
        alias="_id",
        example="60c72b2f9b1e8b001c8e4d5a",
    )
    name: str = Field(..., min_length=2, max_length=100, example="John Doe")
    username: str = Field(..., min_length=3, max_length=50, example="john_doe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    phone_number: str = Field(..., min_length=10, max_length=15, example="+1234567890")
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        example="strongpassword123",
        description="Password must be at least 8 characters long.",
>>>>>>> af3ec91 (Implemented user registration router)
    )

    model_config = ConfigDict(
        title="UserRegistration",
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "username": "john_doe",
                "email": "john.doe@example.com",
                "phone_number": "+1234567890",
<<<<<<< HEAD
                "password": "strongpassword123"
=======
                "password": "strongpassword123",
>>>>>>> af3ec91 (Implemented user registration router)
            }
        },
        validate_by_name=True,
        arbitrary_types_allowed=True,
<<<<<<< HEAD
    )
=======
    )

class UserRegistrationResponse(BaseModel):
    message: str
    data: UserRegistration
>>>>>>> af3ec91 (Implemented user registration router)
