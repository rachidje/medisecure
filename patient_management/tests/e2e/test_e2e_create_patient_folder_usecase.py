import base64
from httpx import ASGITransport, AsyncClient
import pytest

from patient_management.domain.dtos.patient_dto import PatientDTO
from shared.tests.fixtures.seeds.user_seeds import E2eUsers
from shared.tests.test_app import TestApp

@pytest.mark.e2e
@pytest.mark.asyncio
class TestE2ECreatePatientFolderUseCase:
    # pylint: disable=W0201
    def setup_method(self):
        self.test_app = TestApp()
        self.test_app.setup()

        self.test_app.load_fixtures([
            E2eUsers.doctor, 
            E2eUsers.lab_technician_unauthorized,
        ])

        self.payload= PatientDTO.model_validate({
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "date_of_birth": "1990-01-01",
            "consent": True,
            "guardian_consent": True
        })

    async def test_should_return_patient_id(self):
        self.token = base64\
                    .b64encode(f"{E2eUsers.doctor.entity.email}:{E2eUsers.doctor.entity.password}"\
                                .encode("utf-8"))\
                    .decode("utf-8")
        transport = ASGITransport(app= self.test_app.app)

        async with AsyncClient(transport= transport, base_url="http://test") as client:
            response = await client.post(
                url="/patient/", 
                headers={"Authorization": f"Basic {self.token}"},
                json= self.payload.model_dump(mode="json")
                )
            
            assert response.status_code == 201
            assert isinstance(response.json()['id'], str )
        
    async def test_should_fail_with_unauthorized_role(self):
        self.token = base64\
                    .b64encode(f"{E2eUsers.lab_technician_unauthorized.entity.email}:{E2eUsers.lab_technician_unauthorized.entity.password}"\
                            .encode("utf-8"))\
                    .decode("utf-8")

        transport = ASGITransport(app= self.test_app.app)

        async with AsyncClient(transport= transport, base_url="http://test") as client:
            response = await client.post(
                url="/patient/", 
                headers={"Authorization": f"Basic {self.token}"},
                json= self.payload.model_dump(mode="json")
                )
            print(response.json())
            assert response.status_code == 401
            assert 'User does not have the required role' in response.json()['detail']
