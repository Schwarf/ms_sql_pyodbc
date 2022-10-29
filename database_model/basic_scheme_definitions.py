from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from base import naming_convention

BaseDefinition = declarative_base(metadata=MetaData(naming_convention=naming_convention))
metadata = BaseDefinition.metadata

