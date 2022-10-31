from sqlalchemy import Column, ForeignKey, Integer, String, Table

from database_model.basic_scheme_definitions import InsertionDateTime
from database_model.scheme_definitions import SchemeDefinition, metadata


class VisitedWebsites(SchemeDefinition, InsertionDateTime):
    __tablename__ = "VisitedWebsites"
    internal_id = Column(Integer, primary_key=True)
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)
    root_url = Column(String(1000), nullable=False)
    root_url_hash = Column(Integer, nullable=False)
    keywords = Column(String())

