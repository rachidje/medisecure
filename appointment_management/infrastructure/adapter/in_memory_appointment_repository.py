from appointment_management.domain.entities.appointment import Appointment


class InMemoryAppointmentRepository:
    def __init__(self):
        self.appointments: list[Appointment] = []

    def find_by_professional_id(self, professional_id: str) -> list[Appointment]:
        return [appointment for appointment in self.appointments if appointment.professional_id == professional_id]
    
    def create(self, appointment: Appointment) -> None:
        self.appointments.append(appointment)