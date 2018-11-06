from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    shows = relationship('Show', secondary='show_songs')
