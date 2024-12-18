from fastapi import FastAPI

from api.routers import patient_router

api_app = FastAPI()

api_app.include_router(patient_router.router)