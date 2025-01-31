from typing import Protocol

from appointment_management.domain.entities.appointment import Appointment


class AppointmentRepositoryProtocol(Protocol):
    def find_by_professional_id(self, professional_id: str) -> list[Appointment]: ...
    def create(self, appointment: Appointment) -> None: ...