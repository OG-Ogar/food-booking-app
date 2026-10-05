from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


security = HTTPBearer()

from utils.jwt import decode_access_token


def get_current_customer(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    customer_id = payload.get("sub")

    if customer_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return int(customer_id)