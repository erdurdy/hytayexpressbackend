from src.database import Base
from sqlalchemy import  Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"

    id = Column("id",Integer, primary_key=True, index=True)
    username = Column("username", String(50))
    password = Column("password", String(50))
    email = Column("email", String(50))
    is_ative = Column("is_ative", Boolean, default=False)
    is_star = Column("is_star", Boolean, default=False)
    ver_number = Column("ver_number", Integer(50))
    