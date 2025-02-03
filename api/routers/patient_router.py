from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from api.middlewares.authentication_middleware import authentication_middleware
from patient_management.application.usecases.create_patient_folder_usecase\
    import PatientDataPayload
from patient_management.domain.dtos.patient_dto import PatientDTO
from patient_management.infrastructure.adapter.primary.controllers.patient_controller\
    import PatientController
from shared.container.container import Container
from shared.domain.entities.user import User

router = APIRouter(prefix="/patient", tags=["Patient"])

@router.post("/")
@inject
async def create_patient(
    data: PatientDTO, 
    user: User = Depends(authentication_middleware),
    controller: PatientController = Depends(Provide[Container.patient_controller])
):
    payload = PatientDataPayload(**data.model_dump(), medical_professional=user)
    patient_id = controller.create(payload)
    return JSONResponse({"id": patient_id}, 201)
