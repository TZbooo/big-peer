from passlib.apache import HtpasswdFile
from fastapi import APIRouter, HTTPException, Depends

from .auth import verify_static_token
from ..schemas.user import CreateUserSchema


router = APIRouter(
    prefix='/user',
    dependencies=[Depends(verify_static_token)]
)


@router.post('/add')
async def add_proxy_user(user: CreateUserSchema):
    ht = HtpasswdFile('/etc/squid/passwords')
    if user.username not in ht.users():
        ht.set_password(user.username, user.password)
        ht.save()
        return {'success': True}
    raise HTTPException(
        status_code=409,
        detail='user already exists'
    )


@router.delete('/delete')
async def delete_proxy_user(username: str):
    ht = HtpasswdFile('/etc/squid/passwords')
    if username in ht.users():
        ht.delete(username)
        ht.save()
        return {'success': True}
    raise HTTPException(
        status_code=404,
        detail='user does not exists'
    )