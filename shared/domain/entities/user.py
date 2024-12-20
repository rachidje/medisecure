from pydantic import BaseModel

from shared.domain.enum.roles_enum import Role


class User(BaseModel):
    id: str
    firstname: str
    lastname: str
    email: str
    password: str
    roles: list[Role]