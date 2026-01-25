from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)

    # Core shift info
    date = Column(String, nullable=False)      # "YYYY-MM-DD"
    start = Column(String, nullable=False)     # "09:00"
    end = Column(String, nullable=False)       # "17:00"
    site = Column(String, default="")
    role = Column(String, default="")

    # Capacity + claiming
    slots = Column(Integer, default=1)
    claimed = Column(Integer, default=0)

    # Optional
    pay = Column(Float, nullable=True)


