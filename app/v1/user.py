from passlib.apache import HtpasswdFile
from fastapi import APIRouter

from ..schemas.user import UserSchema


router = APIRouter(
    prefix='/user'
)


@router.post('/add')
async def add_proxy_user(user: UserSchema):
    ht = HtpasswdFile('/etc/squid/passwords')
    if user.username not in ht.users():
        ht.set_password(user.username, user.password)
        ht.save()
        return {'success': True}
    return {
        'success': False,
        'error': 'user already exists'
    }


@router.delete('/delete')
async def delete_proxy_user(username: str):
    ht = HtpasswdFile('/etc/squid/passwords')
    if username in ht.users():
        ht.delete(username)
        ht.save()
        return {'success': True}
    return {
        'success': True,
        'error': 'user does not exists'
    }