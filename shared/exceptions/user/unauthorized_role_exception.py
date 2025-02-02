class UnauthorizedRoleException(Exception):
    def __init__(self):
        super().__init__("User does not have the required role")
