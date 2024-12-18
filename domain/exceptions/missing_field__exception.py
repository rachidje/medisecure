class MissingFieldException(Exception):
    def __init__(self, field: str):
        self.field = field
        super().__init__(f"Missing required field: {field}")