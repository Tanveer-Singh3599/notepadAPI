from database import Base
from sqlalchemy import String, Column

class Notes(Base):
    __tablename__ = "Notes"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    note = Column(String, nullable=True)