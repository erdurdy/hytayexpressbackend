from fastapi import APIRouter, Depends
from src.database import get_db
from src.schemas.Container import CreateContainer, ViewContainer
from src.models.Container import Container as ContainerModel
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/container",
    tags=["Container"],
    responses={404: {"description": "Not found"}}
)





@router.get("/all")
def get_all(db: Session = Depends(get_db)): 
    data_list = db.query(ContainerModel).all()
    return data_list

@router.get("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    data =  db.query(ContainerModel).filter(ContainerModel.id == id).first()
    return ViewContainer.from_orm(data)


@router.post("/")
def get_offer(details: CreateContainer, db: Session = Depends(get_db)):
    print(details)
    new_data = ContainerModel(**details.dict())
    
    db.add(new_data)
    db.commit()
    return ViewContainer.from_orm(new_data)

@router.delete("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    try:
        db.query(ContainerModel).filter(ContainerModel.id == id).delete()
        db.commit()
    except Exception as e:
        print(e)
    
    return {"status":"success"}