from sqlalchemy import Column, ForeignKey, Integer, String, Table

from database_model.basic_scheme_definitions import InsertionDateTime
from database_model.scheme_definitions import SchemeDefinition, metadata


class RootWebsites(SchemeDefinition, InsertionDateTime):
    __tablename__ = "RootWebsites"

    internal_id = Column(Integer, primary_key=True)
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)


class VisitedWebsites(SchemeDefinition, InsertionDateTime):
    __tablename__ = "VisitedWebsites"

    internal_id = Column(Integer, primary_key=True)
    root_website_id = Column(ForeignKey("RootWebsites.internal_id"))
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)


WebsiteMetadata = Table("WebsiteMetadata", metadata,
    Column('website_id', ForeignKey("VisitedWebsites.internal_id")),
    Column('title', String(1000), nullable=False),
    Column('contained_urls', String()))
