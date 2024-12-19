from fastapi import HTTPException, Request
from shared.adapters.secondary.in_memory_user_repository import InMemoryUserRepository
from shared.domain.entities.user import User
from shared.services.authenticator.basic_authenticator import BasicAuthenticator
from shared.services.authenticator.extract_token import AuthenticatorUtility


user_repository = InMemoryUserRepository()
authenticator = BasicAuthenticator(user_repository)

async def authentication_middleware(request: Request) -> User:
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