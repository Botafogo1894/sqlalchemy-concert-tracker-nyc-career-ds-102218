from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    venues = relationship('Venue', back_populates = 'city')
