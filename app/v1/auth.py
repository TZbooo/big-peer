import os

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

token_header = APIKeyHeader(name='Authorization')
real_token = os.getenv('PROXY_MANAGER_TOKEN')


async def verify_static_token(token = Security(token_header)) -> bool:
    if token != real_token:
        raise HTTPException(
            status_code=401,
            detail='Not Authorized'
        )
    return True