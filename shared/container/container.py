from dependency_injector import providers, containers

from patient_management.application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase
from patient_management.infrastructure.adapter.primary.controllers.patient_controller import PatientController
from patient_management.infrastructure.adapter.secondary.in_memory_patient_repository import InMemoryPatientRepository
from shared.adapters.secondary.in_memory_user_repository import InMemoryUserRepository
from shared.adapters.secondary.uuid_generator import UUIDGenerator
from shared.services.authenticator.basic_authenticator import BasicAuthenticator

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # 📦 Infrastructure
    patient_repository = providers.Singleton(InMemoryPatientRepository)
    user_repository = providers.Singleton(InMemoryUserRepository)
    id_generator = providers.Singleton(UUIDGenerator)

    # 📦 Application
    create_patient_folder_usecase = providers.Factory(
        CreatePatientFolderUseCase,
        patient_repository=patient_repository,
        id_generator=id_generator
    )

    # 📦 Services
    authenticator = providers.Singleton(
        BasicAuthenticator,
        user_repository=user_repository
    )

    # 📦 Controllers
    patient_controller = providers.Factory(
        PatientController,
        usecase = create_patient_folder_usecase
    )