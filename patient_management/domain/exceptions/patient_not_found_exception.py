class PatientNotFoundException(Exception):
    def __init__(self, data: str):
        self.data = data
        super().__init__(f"Patient with following information: {data} not found")