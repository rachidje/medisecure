from datetime import date, time
import pytest

from appointment_management.application.usecases.schedule_appointment import ScheduleAppointmentUseCase
from appointment_management.domain.entities.appointment import Appointment
from appointment_management.domain.exceptions.not_available_professional_exception import NotAvailableProfessionalException
from appointment_management.domain.exceptions.outside_opening_hours_exception import OutsideOpeningHoursException
from appointment_management.infrastructure.adapter.in_memory_appointment_repository import InMemoryAppointmentRepository
from shared.adapters.secondary.fixed_id_generator import FixedIDGenerator

@pytest.mark.unittest
class TestScheduleAppointment:
    def setup_method(self):
        self.appointment_repository = InMemoryAppointmentRepository()
        self.id_generator = FixedIDGenerator()
        self.usecase = ScheduleAppointmentUseCase(self.appointment_repository, self.id_generator)

    def test_should_fail_if_professional_is_not_available(self):
        self.appointment_repository.create(
            Appointment(
                id="appointment_1",
                patient_id="patient_1",
                professional_id="professional_1",
                date=date(2024, 1, 1),
                start_time=time(9, 0),
                end_time=time(10, 0)
            )
        )

        with pytest.raises(NotAvailableProfessionalException):
            self.usecase.execute({
                'patient_id': "patient_1",
                'professional_id': "professional_1",
                "date": date(2024, 1, 1),
                "start_time": time(9, 0),
                "end_time": time(10, 0)
            })

    def test_should_fail_outside_of_opening_hours(self):
        with pytest.raises(OutsideOpeningHoursException):
            self.usecase.execute({
                'patient_id': "patient_1",
                'professional_id': "professional_1",
                "date": date(2024, 1, 1),
                "start_time": time(19, 0),
                "end_time": time(20, 0)
            })

    def test_should_fail_if_patient_has_appointment_at_same_time(self):
        ...

    def test_should_fail_if_appointment_made_less_than_24_hours_before(self):
        ...

    def test_should_make_appointment(self):
        ...

    def test_should_notify_patient_and_professional(self):
        ...

    

