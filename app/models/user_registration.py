from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import Optional
from bson import ObjectId

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
                "password": "strongpassword123"
            }
        },
        validate_by_name=True,
        arbitrary_types_allowed=True,
    )