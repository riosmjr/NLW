from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nulable=False)
    maximum_attendees = Column(Integer)