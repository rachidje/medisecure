class MissingGuardianConsentException(Exception):
    def __init__(self):
        super().__init__("Unable to create folder without guardian consent for minor")