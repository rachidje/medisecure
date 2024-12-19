from uuid import uuid4


class UUIDGenerator:
    def generate(self):
        return uuid4().hex