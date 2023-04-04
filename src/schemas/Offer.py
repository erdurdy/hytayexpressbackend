from pydantic import BaseModel

class OfferSchema(BaseModel):
    fullname: str
    number: int
    email: str
    address: str
    offer:str

    class Config:
        orm_mode=True

class CreateOffer(BaseModel):
    fullname: str
    number: int
    email: str
    address: str
    offer:str
    
    class Config:
        orm_mode=True
    
