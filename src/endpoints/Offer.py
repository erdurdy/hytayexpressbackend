from fastapi import APIRouter, Depends
from src.database import SessionLocal, get_db
from src.schemas.Offer import CreateOffer, ViewOffer
from src.models.Offer import Offer as OfferModel
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/offer",
    tags=["Offer"],
    responses={404: {"description": "Not found"}}
)





@router.get("/all")
def get_all(db: Session = Depends(get_db)): 
    data_list = db.query(OfferModel).all()
    return data_list

@router.get("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    data =  db.query(OfferModel).filter(OfferModel.id == id).first()
    return ViewOffer.from_orm(data)


@router.post("/")
def get_offer(details: CreateOffer, db: SessionLocal = Depends(get_db)):
    print(details)
    new_data = OfferModel(**details.dict())
    
    db.add(new_data)
    db.commit()
    return ViewOffer.from_orm(new_data)

@router.delete("/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    try:
        db.query(OfferModel).filter(OfferModel.id == id).delete()
        db.commit()
    except Exception as e:
        print(e)
    
    return {"status":"success"}