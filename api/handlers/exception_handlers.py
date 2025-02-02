from fastapi import Request
from fastapi.responses import JSONResponse

async def unauthorized_exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code= 401,
        content= {
            "detail": exc.args[0]
        }
    )
