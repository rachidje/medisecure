from typing import Protocol
from dependency_injector.wiring import Container

class FixtureProtocol(Protocol):
    def load(self, container: Container) -> None: ...
