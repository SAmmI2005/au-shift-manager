from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .db import Base, engine, get_db
from .models import Shift
from .schemas import ParseRequest, ParseResponse, ShiftOut, ClaimRequest
from .parser import parse_shifts

# Create tables on startup (MVP)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow React dev server (Vite default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/parse", response_model=ParseResponse)
def parse_and_create(req: ParseRequest, db: Session = Depends(get_db)):
    parsed = parse_shifts(req.text)
    if not parsed:
        return {"shifts": []}

    created = []
    for item in parsed:
        s = Shift(**item)
        db.add(s)
        db.flush()   # assigns s.id before commit
        created.append(s)

    db.commit()
    return {"shifts": created}

@app.get("/shifts", response_model=list[ShiftOut])
def list_shifts(db: Session = Depends(get_db)):
    return db.query(Shift).order_by(Shift.id.desc()).all()

@app.post("/shifts/{shift_id}/claim", response_model=ShiftOut)
def claim_shift(shift_id: int, req: ClaimRequest, db: Session = Depends(get_db)):
    s = db.query(Shift).get(shift_id)
    if not s:
        raise HTTPException(status_code=404, detail="Shift not found")

    if s.claimed >= s.slots:
        raise HTTPException(status_code=400, detail="Shift already filled")

    # MVP: just increment claimed count (we’ll store who claimed later)
    s.claimed += 1
    db.commit()
    db.refresh(s)
    return s

