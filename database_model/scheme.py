from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from basics import InsertionDateTime
from scheme_definitions import SchemeDefinition


class RootWebsites(SchemeDefinition, InsertionDateTime):
    __tablename__ = "RootWebsites"

    internal_id = Column(Integer, primary_key=True)
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)

class VisitedWebsites(SchemeDefinition, InsertionDateTime):
    __tablename__ = "VisitedWebsites"

    internal_id = Column(Integer, primary_key=True)
    rootwebsite_id = Column(ForeignKey("RootWebsites.internal_id"))
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)



