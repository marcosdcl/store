from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from utils.validators import validate_type, validate_not_empty, validate_len

Base = declarative_base()

class Category(Base):
    ''' The declarative model class for a Category object. '''
    __tablename__ = 'categories'

    id_ = Column('id', Integer, primary_key = True, nullable = False)
    name = Column('name', String(length=100), nullable = False)
    description = Column('description', String(length=255), nullable = True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name: str) -> str:
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        name = validate_len(name, 100, key)
        return name

    @validates('description')
    def validate_description(self, key, description: str) -> str:
        description = validate_type(description, str, key)
        description = validate_len(description, 255, key)
        return description
