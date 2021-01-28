from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Category(Base):
    ''' The declarative model class for a Category object. '''
    __tablename__ = 'categories'

    id_ = Column('id', Integer, primary_key = True, nullable = False)
    name = Column('name', String(length=100), nullable = False)
    description = Column('description')

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('The name attribute must be a string.')
        if not name.strip():
            raise ValueError('The name attribute cannot be empty.')
        if len(name) > 100:
            raise ValueError(
                'The name attribute must be a maximum of 100 characters.'
                )
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) > 100:
            raise ValueError(
                'The name attribute must be a maximum of 100 characters.'
                )
        return description
