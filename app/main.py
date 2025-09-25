from fastapi import FastAPI, Depends
from app.routes import nutrition

app = FastAPI()

app.include_router(nutrition.router)

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}