from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from api.middlewares.authentication_middleware import authentication_middleware
from patient_management.application.usecases.create_patient_folder_usecase import PatientDataPayload
from patient_management.domain.dtos.patient_dto import PatientDTO
from patient_management.infrastructure.adapter.primary.controllers.patient_controller import PatientController
from shared.domain.entities.user import User



router = APIRouter(prefix="/patient", tags=["Patient"])
controller = PatientController()

@router.post("/")
async def create_patient(data: PatientDTO, user: User = Depends(authentication_middleware)):
    payload = PatientDataPayload(**data.model_dump(), medical_professional=user)
    patient_id = controller.create(payload)
    return JSONResponse({"id": patient_id}, 201)