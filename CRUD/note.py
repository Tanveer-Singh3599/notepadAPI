from sqlalchemy.orm import Session
from schemas import GetNotes
from models import Notes

def get_notes(db: Session):
    notes = db.query(Notes).all()
    return notes

def create_note(request: GetNotes, db: Session):
    new_note = Notes(**request.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return 1



def update_note(request: GetNotes, db: Session):
    query = db.query(Notes).filter(Notes.id == request.id)
    query.update(request.model_dump())
    db.commit()
    return 1


def delete_note(id: str, db: Session):
    query = db.query(Notes).filter(Notes.id == id)
    query.delete(synchronize_session=False)
    db.commit()
    return 1