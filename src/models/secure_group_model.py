from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .user_model import user_secure_group_association

Base = declarative_base()

class SecureGroupModel(Base):
    __tablename__ = 'secure_groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    key_pair = Column(String, nullable=False)

    users = relationship('User', secondary=user_secure_group, back_populates='secure_groups')
    files = relationship("File", back_populates="secure_group")  # One-to-Many with File
