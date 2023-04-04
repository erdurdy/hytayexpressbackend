from src.database import Base
from sqlalchemy import  Column, Integer, DateTime, ForeignKey, String, Boolean, Text
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column("id",Integer, primary_key=True, index=True)
    name = Column("name", String(100))
    fullname = Column("fullname", String(100))
    phone_number = Column("phone_number", Integer)
    filter_number = Column("filter_number", String(50))
    email = Column("email", String)
    product_price = Column("product_price", String)
    created = Column("created", DateTime, default=datetime.now())
    end_date = Column("end_date", DateTime)
    transportId = Column("transportId", Integer, ForeignKey("transports.id"))
    countryId = Column("countryId", Integer, ForeignKey("countries.id"))
    districtId = Column("districtId", Integer, ForeignKey("districts.id"))
    about = Column("about", Text)
    is_active = Column("is_active", Boolean, default=False)
    is_moved = Column("is_moved", Boolean, default=False)
    