from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    password: str

class DeleteUserSchema(BaseModel):
    username: str
