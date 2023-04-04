from src.database import Base
from sqlalchemy import  Column, Integer, String


class ActionType(Base):
    __tablename__ = "actiontypes"

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("name", String)
    order_number = Column("order_number", Integer)
    
    