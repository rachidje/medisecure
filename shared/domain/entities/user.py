from pydantic import BaseModel

from shared.domain.enum.roles_enum import Role


class User(BaseModel):
    id: str
    email: str
    password: str
    roles: list[Role]