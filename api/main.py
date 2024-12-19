from fastapi import FastAPI

from api.handlers.exception_handlers import unauthorized_exception_handler
from api.routers import patient_router
from shared.exceptions.user.unauthorized_role_exception import UnauthorizedRoleException

api_app = FastAPI()

api_app.add_exception_handler(UnauthorizedRoleException, unauthorized_exception_handler)
api_app.include_router(patient_router.router)