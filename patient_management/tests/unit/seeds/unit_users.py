from shared.domain.entities.user import User
from shared.domain.enum.roles_enum import Role


class UnittestUsers:
    medical_professional = User(
        id="1",
        email="johndoe@gmail.com",
        password="qwerty",
        roles= [Role.DOCTOR]
    )