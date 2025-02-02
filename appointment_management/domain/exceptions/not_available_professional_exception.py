class NotAvailableProfessionalException(Exception):
    def __init__(self, professional_id):
        self.professional_id = professional_id
        super().__init__(f"Professional with id: {professional_id} is not available")
