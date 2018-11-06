from base import Base
from sqlalchemy import *
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

class ShowSong(Base):
    __tablename__ = 'show_songs'
    id = Column(Integer, primary_key = True)
    length = Column(Integer)
    notes = Column(String(450000))
    show_id = Column(Integer, ForeignKey('shows.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)
