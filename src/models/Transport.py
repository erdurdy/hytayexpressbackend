from src.database import Base
from sqlalchemy import  Column, Integer, String


class Transport(Base):
    __tablename__ = "transports"

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("name", String(100))
    order_number = Column("order_number", Integer)
    price = Column("price", Integer)
    