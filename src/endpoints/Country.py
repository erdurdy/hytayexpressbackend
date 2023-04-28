from fastapi import APIRouter, Depends
from src.database import get_db
from src.schemas.Country import CreateCountry, ViewCountry
from src.models.Country import Country as CountryModel
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/country",
    tags=["Country"],
    responses={404: {"description": "Not found"}}
)





@router.get("/all")
def get_all(db: Session = Depends(get_db)): 
    data_list = db.query(CountryModel).all()
    return data_list

@router.get("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    data =  db.query(CountryModel).filter(CountryModel.id == id).first()
    return ViewCountry.from_orm(data)


@router.post("/")
def get_offer(details: CreateCountry, db: Session = Depends(get_db)):
    print(details)
    new_data = CountryModel(**details.dict())
    
    db.add(new_data)
    db.commit()
    return ViewCountry.from_orm(new_data)

@router.delete("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    try:
        db.query(CountryModel).filter(CountryModel.id == id).delete()
        db.commit()
    except Exception as e:
        print(e)
    
    return {"status":"success"}