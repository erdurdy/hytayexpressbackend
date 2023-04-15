from pydantic import BaseModel

class Offer(BaseModel):
    fullname: str
    phone_number: int 
    email: str
    address: str
    offer:str

    class Config:
        orm_mode=True

class CreateOffer(Offer):
    
    class Config:
        orm_mode=True
        
class ViewOffer(BaseModel):
    id:int
    fullname: str
    phone_number: int 
    email: str
    address: str
    offer:str
    class Config:
        orm_mode=True
    
