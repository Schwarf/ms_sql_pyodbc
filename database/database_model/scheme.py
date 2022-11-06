from sqlalchemy import Column, Integer, String

from database_model.basic_scheme_definitions import InsertionDateTime
from database_model.scheme_definitions import SchemeDefinition


class VisitedWebsites(SchemeDefinition, InsertionDateTime):
    __tablename__ = "VisitedWebsites"
    internal_id = Column(Integer, primary_key=True)
    url_hash = Column(Integer, nullable=False, index=True, unique=True)
    url = Column(String(1000), nullable=False)
    root_url = Column(String(1000), nullable=False)
    root_url_hash = Column(Integer, nullable=False)
    keywords = Column(String())


class TestBooks(SchemeDefinition, InsertionDateTime):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(String(10), nullable=False)
    upc = Column(String(20), nullable=False)
    availability = Column(String(20), nullable=False)
    number_of_copies = Column(Integer, nullable=False)
    url = Column(String(1000), nullable=False)
    image_url = Column(String(1000), nullable=False)

    keywords = Column(String())
