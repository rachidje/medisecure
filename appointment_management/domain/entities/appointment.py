from datetime import date, time
from pydantic import BaseModel


class Appointment(BaseModel):
    id: str
    patient_id: str
    professional_id: str
    date: date
    start_time: time
    end_time: time

    def is_outside_opening_hours(self):
        return self.start_time < time(8, 0) or self.end_time > time(18, 0)