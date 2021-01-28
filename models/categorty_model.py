from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


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
