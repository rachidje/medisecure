from httpx import ASGITransport, AsyncClient
import pytest
from api.main import api_app

from patient_management.domain.dtos.patient_dto import PatientDTO


@pytest.mark.e2e
@pytest.mark.asyncio
class TestE2ECreatePatientFolderUseCase:
    async def test_should_return_patient_id(self):
        payload= PatientDTO.model_validate({
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "date_of_birth": "1990-01-01",
            "consent": True,
            "guardian_consent": True
        })

        transport = ASGITransport(api_app)

        async with AsyncClient(transport= transport, base_url="http://test") as client:
            response = await client.post("/patient/", json=payload.model_dump(mode="json"))
            assert response.status_code == 201
            assert isinstance(response.json()['id'], str )