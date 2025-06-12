from database import Base
from sqlalchemy import String, Column

class Notes(Base):
    __tablename__ = "Notes"

    id = Column(String(5), primary_key=True)
    name = Column(String(50), nullable=False)
    note = Column(String(10000), nullable=True)