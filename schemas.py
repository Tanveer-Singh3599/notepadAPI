from pydantic import BaseModel

class GetNotes(BaseModel):
    id: str
    name: str
    note: str

class SendNotes(GetNotes):
    class Config():
        orm_mode = True