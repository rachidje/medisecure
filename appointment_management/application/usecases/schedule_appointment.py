from typing import TypedDict
from datetime import date, time

from appointment_management.domain.entities.appointment import Appointment
from appointment_management.domain.exceptions.not_available_professional_exception\
    import NotAvailableProfessionalException
from appointment_management.domain.exceptions.outside_opening_hours_exception\
    import OutsideOpeningHoursException
from appointment_management.domain.ports.secondary.appointment_repository_protocol\
    import AppointmentRepositoryProtocol
from shared.ports.secondary.id_generator_protocol import IDGeneratorProtocol

class AppointmentData(TypedDict):
    patient_id: str
    professional_id: str
    date: date
    start_time: time
    end_time: time

class ScheduleAppointmentUseCase:
    def __init__(self, 
                appointment_repository: AppointmentRepositoryProtocol, 
                id_generator: IDGeneratorProtocol
        ):
        self.appointment_repository = appointment_repository
        self.id_generator = id_generator

    def execute(self, data: AppointmentData):
        appointments = self.appointment_repository.find_by_professional_id(data['professional_id'])

        appointment_id = self.id_generator.generate()

        appointment = Appointment(
            id=appointment_id,
            patient_id=data['patient_id'],
            professional_id=data['professional_id'],
            date=data['date'],
            start_time=data['start_time'],
            end_time=data['end_time']
        )

        if appointment.is_not_available(appointments):
            raise NotAvailableProfessionalException(data['professional_id'])

        if appointment.is_outside_opening_hours():
            raise OutsideOpeningHoursException()
