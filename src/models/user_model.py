from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from authentication.user import User

Base = declarative_base()

# Association table for many-to-many relationship between User and SecureGroup
user_secure_group_association = Table(
    'user_secure_group',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('secure_group_id', Integer, ForeignKey('secure_groups.id'), primary_key=True)
)

class UserModel(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    is_superuser = Column(Integer, default=0)

    def __repr__(self):
        return f"<User {self.username}>"
    def __init__(self, username, email, hashed_password, is_active=1, is_superuser=0):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_superuser = is_superuser
