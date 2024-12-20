from shared.domain.entities.user import User
from shared.domain.enum.roles_enum import Role
from shared.tests.fixtures.user_fixture import UserFixture


class E2eUsers:
    doctor = UserFixture(
        User(
            id = "doctor",
            firstname = "Doctor",
            lastname = "Doe",
            email = "doctor@gmail.com",
            password = "doctor",
            roles = [Role.DOCTOR]
        )
    )

    lab_technician_unauthorized = UserFixture(
        User(
            id = "lab_technician_unauthorized",
            firstname = "Lab",
            lastname = "Technician",
            email = "lab_technician_unauthorized@gmail.com",
            password = "lab_technician_unauthorized",
            roles = [Role.LAB_TECHNICIAN]
        )
    )