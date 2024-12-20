import base64
from httpx import ASGITransport, AsyncClient
import pytest
from api.main import api_app, container

from patient_management.domain.dtos.patient_dto import PatientDTO
from shared.domain.entities.user import User
from shared.domain.enum.roles_enum import Role

@pytest.mark.e2e
@pytest.mark.asyncio
class TestE2ECreatePatientFolderUseCase:
    def setup_method(self):

        self.payload= PatientDTO.model_validate({
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "date_of_birth": "1990-01-01",
            "consent": True,
            "guardian_consent": True
        })

        self.professional = User(
            id="1",
            email="johndoe@gmail.com",
            password="qwerty",
            roles= [Role.DOCTOR]
        )

        self.unauthorized_professional = User.model_copy(self.professional, update={"email": "unauthorized@gmail.com", "roles": [Role.LAB_TECHNICIAN]})

        self.container = container


        self.user_repository = self.container.user_repository()
        self.user_repository.create(self.professional)
        self.user_repository.create(self.unauthorized_professional)

    async def test_should_return_patient_id(self):
        self.token = base64.b64encode(f"{self.professional.email}:{self.professional.password}".encode("utf-8")).decode("utf-8")
        transport = ASGITransport(api_app)

        async with AsyncClient(transport= transport, base_url="http://test") as client:
            response = await client.post(
                url="/patient/", 
                headers={"Authorization": f"Basic {self.token}"},
                json= self.payload.model_dump(mode="json")
                )
            
            assert response.status_code == 201
            assert isinstance(response.json()['id'], str )

        
    async def test_should_fail_with_unauthorized_role(self):
        self.token = base64.b64encode(f"{self.unauthorized_professional.email}:{self.unauthorized_professional.password}".encode("utf-8")).decode("utf-8")

        transport = ASGITransport(api_app)

        async with AsyncClient(transport= transport, base_url="http://test") as client:
            response = await client.post(
                url="/patient/", 
                headers={"Authorization": f"Basic {self.token}"},
                json= self.payload.model_dump(mode="json")
                )
            print(response.json())
            assert response.status_code == 401
            assert 'User does not have the required role' in response.json()['detail']