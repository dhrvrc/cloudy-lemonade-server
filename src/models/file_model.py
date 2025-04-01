from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class FileModel(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)
    metadata = Column(String, nullable=True)
    secure_group_id = Column(Integer, ForeignKey('secure_groups.id', ondelete="CASCADE"))

    secure_group = relationship('SecureGroupModel', back_populates='files')