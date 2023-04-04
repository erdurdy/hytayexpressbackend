from src.database import Base
from sqlalchemy import  Column, Integer, DateTime, ForeignKey, String, Boolean
from datetime import datetime

class Container(Base):
    __tablename__ = "containers"

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("name", String)
    created = Column("created", DateTime, default=datetime.now())
    start_date = Column("start_date", DateTime)
    end_date = Column("end_date", DateTime)
    productId = Column("productId", Integer, ForeignKey("products.id"))
    actionId = Column("actionId", Integer, ForeignKey("actions.id"))
    is_active = Column("is_active", Boolean)
    is_moved = Column("is_moved", Boolean)