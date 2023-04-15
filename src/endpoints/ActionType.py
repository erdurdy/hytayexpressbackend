from fastapi import APIRouter, Depends
from src.database import get_db
from src.schemas.ActionType import CreateActionType, ViewActionType
from src.models.ActionType import ActionType as ActionTypeModel
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/actiontype",
    tags=["ActionType"],
    responses={404: {"description": "Not found"}}
)





@router.get("/all", response_model=list[ViewActionType])
def get_all(db: Session = Depends(get_db)): 
    data_list = db.query(ActionTypeModel).all()
    return data_list

@router.get("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    data =  db.query(ActionTypeModel).filter(ActionTypeModel.id == id).first()
    return ViewActionType.from_orm(data)


@router.post("/")
def get_offer(details: CreateActionType, db: Session = Depends(get_db)):
    new_data = ActionTypeModel(**details.dict())
    
    db.add(new_data)
    db.commit()
    return ViewActionType.from_orm(new_data)

@router.delete("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    try:
        db.query(ActionTypeModel).filter(ActionTypeModel.id == id).delete()
        db.commit()
    except Exception as e:
        print(e)
    
    return {"status":"success"}