from patient_management.domain.ports.id_generator_protocol import IDGeneratorProtocol


class FixedIDGenerator(IDGeneratorProtocol):
    def generate(self) -> str:
        return "1"