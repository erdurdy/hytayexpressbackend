from pydantic import BaseModel
from datetime import datetime as time

class Action(BaseModel):

    datetime: time | None = time.now()
    containerId: int | None = None
    actiontypeId: int | None = None
    picture: str
    
class CreateAction(Action):
    
    class Config: orm_mode=True
    
    
class ViewAction(BaseModel):
    id: int
    datetime: time | None = time.now()
    containerId: int | None = None
    actiontypeId: int | None = None
    picture: str
    
    class Config: orm_mode=True