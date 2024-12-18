from typing import Protocol


class IDGeneratorProtocol(Protocol):
    def generate(self) -> str: ...