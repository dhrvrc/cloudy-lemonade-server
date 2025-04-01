from sqlalchemy.orm import Session
from models.user_model import UserModel

class UserRepository:
    @staticmethod
    def create_user(session: Session, user: UserModel):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def get_user_by_id(session: Session, user_id: int):
        return session.query(UserModel).filter(UserModel.id == user_id).first()
