from fastapi import FastAPI
from app.routes.user_registration import router as user_registration_router

app = FastAPI(title="E-commerce Backend API")


app.include_router(user_registration_router)


@app.get("/")
def root():
    return {"message": "E-commerce Backend API is running"}
