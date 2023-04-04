from src.database import Base
from sqlalchemy import  Column, Integer, DateTime, ForeignKey, String


class Action(Base):
    __tablename__ = "actions"

    id = Column("id",Integer, primary_key=True, index=True)
    datetime = Column("datetime", DateTime)
    containerId = Column("containerId", Integer, ForeignKey("containers.id"))
    actiontypeId = Column("actiontypeId", Integer, ForeignKey("actiontypes.id"))
    picture = Column("picture", String)