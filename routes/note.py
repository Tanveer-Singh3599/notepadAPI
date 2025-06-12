from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import GetNotes
from models import Notes
from CRUD import note

router = APIRouter(
    prefix='/note',
    tags=['note']
)

@router.get('/getnotes', status_code=status.HTTP_200_OK)
def get_notes(db: Session = Depends(get_db)):
    return note.get_notes(db)

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_note(request: GetNotes, db: Session = Depends(get_db)):
    try:
        return note.create_note(request, db)
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Insufficient or invalid information")

@router.patch('/update')
def update_note(request: GetNotes, db: Session = Depends(get_db)):
    try:
        return note.update_note(request, db)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found.")

@router.delete('/delete/{id}')
def delete_note(id: str, db: Session = Depends(get_db)):
    try:
        return note.delete_note(id, db)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found.")