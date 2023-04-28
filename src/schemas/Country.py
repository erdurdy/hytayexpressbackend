from pydantic import BaseModel, Field

class CreateCountry(BaseModel):
    name: str = Field(max_length=100)
    order_number: int | None = None
    price: int | None = None
    
    

class ViewCountry(BaseModel):
    id: int
    name: str
    order_number: int | None = None
    price: float | None = None
    
    class Config: orm_mode=True