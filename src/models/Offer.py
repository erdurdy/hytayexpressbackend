from src.database import Base
from sqlalchemy import  Column, Integer, String, Text


class Offer(Base):
    __tablename__ = "offers"

    id = Column("id",Integer, primary_key=True, index=True)
    fullname = Column("fullname", String(100))
    phone_number = Column("phone_number", Integer)
    email = Column("email", String(100))
    address = Column("address", String(250))
    offer = Column("offer", Text)
    