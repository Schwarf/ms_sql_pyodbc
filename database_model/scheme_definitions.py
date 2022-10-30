from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from basics import naming_convention

SchemeDefinition = declarative_base(metadata=MetaData(naming_convention=naming_convention))
metadata = SchemeDefinition.metadata

