from dependency_injector import providers, containers

from patient_management.application.usecases.create_patient_folder_usecase import CreatePatientFolderUseCase
from patient_management.infrastructure.adapter.primary.controllers.patient_controller import PatientController
from patient_management.infrastructure.adapter.secondary.mysql.mysql_patient_repository import MySQLPatientRepository
from shared.adapters.secondary.in_memory_user_repository import InMemoryUserRepository
from shared.adapters.secondary.mysql_db.connection import get_session
from shared.adapters.secondary.uuid_generator import UUIDGenerator
from shared.services.authenticator.basic_authenticator import BasicAuthenticator

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # 📦 Infrastructure
    session = providers.Singleton(get_session)
    patient_repository = providers.Singleton(
        MySQLPatientRepository,
        session=session
    )
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