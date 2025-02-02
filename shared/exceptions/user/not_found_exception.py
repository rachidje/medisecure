class UserNotFoundException(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"User not found with email {email}")
