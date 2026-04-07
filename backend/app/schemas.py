from pydantic import BaseModel
from typing import Optional, List

#  Request bodies 

class ParseRequest(BaseModel):
    text: str

class ClaimRequest(BaseModel):
    employee: str


# Response models

class ShiftOut(BaseModel):
    id: int
    date: str
    start: str
    end: str
    site: str
    role: str
    slots: int
    claimed: int
    pay: Optional[float] = None

    class Config:
        from_attributes = True


class ParseResponse(BaseModel):
    shifts: List[ShiftOut]
