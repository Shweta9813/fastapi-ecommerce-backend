from fastapi import APIRouter, HTTPException, Depends, status

from app.utils.hash import hash_password, verify_password
from app.utils.jwt_utils import create_jwt_token, verify_jwt_token
from app.models.user_registration import UserRegistration, UserRegistrationResponse
from app.database.mongodb import users_collection
from app.services.auth_verification import authenticate_user
from app.models.user_login import UserLogin, UserLoginResponse


router = APIRouter(tags=["User Authentication"])


@router.post(
    "/auth/register",
    response_model=UserRegistrationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Register a new user",
)
def register_user(user: UserRegistration):

    username = user.username.strip().lower()
    email = user.email.strip().lower()

    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    password = user.password.strip()
    hashed_password = hash_password(password)

    user_info = {
        "name": user.name.strip(),
        "username": username,
        "email": email,
        "phone_number": user.phone_number.strip(),
        "password": hashed_password,
    }

    result = users_collection.insert_one(user_info)
    user.id = str(result.inserted_id)
    return {"message": f"User {user.name} registered successfully", "data": user}

@router.post(
    "/auth/login",
    response_model=UserLoginResponse,
    status_code=status.HTTP_200_OK,
    summary="User Login",
    description="Authenticate user and return JWT token",
)

def user_login(user: UserLogin):
    email = user.email.strip().lower()
    password = user.password.strip()

    user_data = authenticate_user(email, password)
    if not user_data:
        raise HTTPException(status_code=404, detail="Invalid email or password")
    token = create_jwt_token(user_data["username"])
    return UserLoginResponse(message="Login successful", token=token)



