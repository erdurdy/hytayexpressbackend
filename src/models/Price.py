from src.database import Base
from sqlalchemy import  Column, Integer


class Price(Base):
    __tablename__ = "prices"

    id = Column("id",Integer, primary_key=True, index=True)
    price = Column("price", Integer)
