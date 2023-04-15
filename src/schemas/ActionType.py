from pydantic import BaseModel

class ActionType(BaseModel):
    name: str 
    order_number: int
    
class CreateActionType(ActionType):
    
    class Config: orm_mode=True
    

class ViewActionType(BaseModel):
    id: int
    name: str 
    order_number: int
    
    class Config: orm_mode=True