from app.database.mongodb import users_collection
from app.utils.hash import verify_password
from fastapi import HTTPException


def authenticate_user(username: str, password: str) -> str:
    """
    Authenticate a user by verifying the username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        str: The JWT token if authentication is successful.
    """

    user = users_collection.find_one({"username": username})
    if user and verify_password(password, user["password"]):
        return user
    raise HTTPException(status_code=404, detail="User not found")
