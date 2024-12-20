from sqlalchemy.orm import Session
from shared.domain.entities.user import User
from shared.domain.models.user_model import UserModel
from shared.ports.secondary.user_repository_protocol import UserRepositoryProtocol


class MySQLUserRepository(UserRepositoryProtocol):
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def create(self, user: User):
        model = UserModel(
            id= user.id,
            firstname= user.firstname,
            lastname= user.lastname,
            email= user.email,
            password= user.password,
            roles= user.roles
        )
        self.session.add(model)
        self.session.commit()
    
    def find_by_id(self, id: str) -> User | None:
        model = self.session.query(UserModel).filter_by(id= id).first()
        
        return User(
            id= model.id,
            firstname= model.firstname,
            lastname= model.lastname,
            email= model.email,
            password= model.password,
            roles= model.roles
        ) if model else None
    
    def find_by_email(self, email: str) -> User | None:
        model = self.session.query(UserModel).filter_by(email= email).first()
        
        return User(
            id= model.id,
            firstname= model.firstname,
            lastname= model.lastname,
            email= model.email,
            password= model.password,
            roles= model.roles
        ) if model else None