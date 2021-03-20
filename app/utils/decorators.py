from fastapi import Header, HTTPException

from models.schemas import JwtToken
from utils.jwt_helper import JWTHelper


async def verify_token(authorization: str = Header(...)):
    try:
        jtw_token = JwtToken(**JWTHelper.decode_token(authorization))
        return jtw_token
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")
