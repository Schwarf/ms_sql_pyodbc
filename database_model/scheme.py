from sqlalchemy import Column, ForeignKey, Integer, String

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
    root_website_id = Column(ForeignKey("RootWebsites.internal_id"))
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)


class WebsiteMetadata(SchemeDefinition, InsertionDateTime):
    __tablename__ = "WebsiteMetadata"
    website_id = Column(ForeignKey("VisitedWebsites.internal_id"))
    title = Column(String(1000), nullable=False)
    contained_urls = Column(String())
