from shared.ports.secondary.id_generator_protocol import IDGeneratorProtocol


class FixedIDGenerator(IDGeneratorProtocol):
    def generate(self) -> str:
        return "1"