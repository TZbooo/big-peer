from fastapi import FastAPI

from .v1 import user


app = FastAPI()
app.include_router(user.router)