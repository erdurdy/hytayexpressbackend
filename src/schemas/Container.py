from pydantic import BaseModel
from datetime import datetime as time


class Container(BaseModel):
    name: str
    created: time | None = time.now()
    start_date: time | None = time.now()
    end_date: time | None = time.now()
    is_active: bool | None = False
    is_moved: bool | None = False
    
    
class CreateContainer(Container):
    
    class Config: orm_mode=True
    
    
class ViewContainer(BaseModel):
    id: int
    name: str
    created: time | None = time.now()
    start_date: time | None = time.now()
    end_date: time | None = time.now()
    is_active: bool | None = False
    is_moved: bool | None = False
    
    class Config: orm_mode=True