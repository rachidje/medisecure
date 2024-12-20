from fastapi import FastAPI

from api.handlers.exception_handlers import unauthorized_exception_handler
from api.routers import patient_router
from shared.container.container import Container
from shared.exceptions.user.unauthorized_role_exception import UnauthorizedRoleException

api_app = FastAPI()

container = Container()

container.wire(
    modules=[
        "api.routers.patient_router",
        "api.middlewares.authentication_middleware"
    ]
)

api_app.add_exception_handler(UnauthorizedRoleException, unauthorized_exception_handler)
api_app.include_router(patient_router.router)