from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    shows = relationship('Show', back_populates = 'bands')
