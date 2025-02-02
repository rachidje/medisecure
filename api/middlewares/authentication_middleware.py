from fastapi import Depends, HTTPException, Request
from dependency_injector.wiring import inject, Provide
from shared.container.container import Container
from shared.domain.entities.user import User
from shared.ports.secondary.authenticator_protocol import AuthenticatorProtocol
from shared.services.authenticator.extract_token import AuthenticatorUtility


@inject
async def authentication_middleware(
    request: Request,
    authenticator: AuthenticatorProtocol = Depends(Provide[Container.authenticator])
    ) -> User:
    credentials = request.headers.get("Authorization")

    if not credentials:
        raise HTTPException(status_code=403, detail="Authentication credentials were not found")

    token = AuthenticatorUtility.extract_token(credentials)
    if not token:
        raise HTTPException(status_code=403, detail="Invalid authentication credentials")

    user = authenticator.authenticate(token)

    if not user:
        raise HTTPException(status_code=403, detail="Invalid authentication credentials")

    request.state.user = user
    return user
