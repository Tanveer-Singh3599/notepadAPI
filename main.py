from fastapi import FastAPI
from database import engine, Base
from routes import note

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(note.router)