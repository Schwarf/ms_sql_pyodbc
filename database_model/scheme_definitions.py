from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from database_model.basic_scheme_definitions import naming_convention

SchemeDefinition = declarative_base(metadata=MetaData(naming_convention=naming_convention))
metadata = SchemeDefinition.metadata

