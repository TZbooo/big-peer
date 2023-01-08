from fastapi import FastAPI

from .db.session import init_db, wait_for_db


app = FastAPI()


@app.on_event('startup')
def on_startup():
    wait_for_db()
    init_db()