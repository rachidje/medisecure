class AuthenticatorUtility:
    @staticmethod
    def extract_token(authorization_header: str) -> str | None:
        prefix, token = authorization_header.split(" ")
        if prefix.lower() not in ["basic", "bearer"]:
            return None
        return token