from fastapi import HTTPException, status  

from app.database.mongodb import users_collection
from app.utils.hash import verify_password


def authenticate_user(email: str, password: str) -> str:
    """
    Authenticate a user by verifying the email and password.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        str: The JWT token if authentication is successful.
    """

    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    if not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password."
        )
    return user
