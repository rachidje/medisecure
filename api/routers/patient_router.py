from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from patient_management.application.usecases.create_patient_folder_usecase import PatientDataPayload
from patient_management.domain.dtos.patient_dto import PatientDTO
from patient_management.infrastructure.adapter.primary.controllers.patient_controller import PatientController



router = APIRouter(prefix="/patient", tags=["Patient"])
controller = PatientController()

@router.post("/")
async def create_patient(data: PatientDTO):
    try:
        payload = PatientDataPayload(**data.model_dump())
        patient_id = controller.create(payload)
        return JSONResponse({"id": patient_id}, 201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))