from fastapi import APIRouter, Depends
from src.database import SessionLocal, get_db
from src.schemas.Action import CreateAction, ViewAction
from src.models.Action import Action as ActionModel
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/action",
    tags=["Action"],
    responses={404: {"description": "Not found"}}
)





@router.get("/all")
def get_all(db: Session = Depends(get_db)): 
    data_list = db.query(ActionModel).all()
    return data_list

@router.get("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    data =  db.query(ActionModel).filter(ActionModel.id == id).first()
    return ViewAction.from_orm(data)

from datetime import datetime as time
from fastapi import File, UploadFile, Body, Form, Depends
from pathlib import Path
import shutil
from pydantic import BaseModel
import json

class ActionSchema(BaseModel):
    name: str
    # number: int
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

@router.post("/")
async def get_offer(action: str = Form(...), file: UploadFile | None = File(None)):
# def get_offer(
#     image: bytes, datetime: time | None = None, containerId: int | None = None,
#     actiontypeId: int | None = None, db: SessionLocal = Depends(get_db)):
    print(action)
    print(file.filename)
    
    
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # return {"filename": file.filename}
    # new_data = ActionModel(**details.dict())
    
    # db.add(new_data)
    # db.commit()
    # return ViewAction.from_orm(new_data)
    return {"status":"success"}

@router.delete("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    try:
        db.query(ActionModel).filter(ActionModel.id == id).delete()
        db.commit()
    except Exception as e:
        print(e)
    
    return {"status":"success"}