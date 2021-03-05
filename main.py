from typing import Optional

from fastapi import FastAPI
from items import rooms
app = FastAPI()
cuartos = rooms()


@app.get("/rooms")
def read_rooms():
    return cuartos
