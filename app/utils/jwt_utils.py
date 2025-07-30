from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional

from config import settings

security = HTTPBearer()


def create_jwt_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    payload = {
        "username": username,
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }
    token = jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return token


def verify_jwt_token(token: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    try:
        token = jwt.decode(
            token.credentials,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        if "username" not in token:
            raise HTTPException(status_code=401, detail="Invalid token")
        return token
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while verifying the token: {str(e)}",
        )
