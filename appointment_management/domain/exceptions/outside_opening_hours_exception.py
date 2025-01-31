class OutsideOpeningHoursException(Exception):
    def __init__(self):
        super().__init__("Appointment outside of opening hours")