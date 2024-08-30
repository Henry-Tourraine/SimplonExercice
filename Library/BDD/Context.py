from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import inspect
from functools import wraps
from .utils import Filter
from sqlalchemy.orm import joinedload
import types


SQLALCHEMY_DATABASE_URL = "sqlite:///library.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def build_filters(self, model, filters: list[Filter], options:bool=False):
      query = self.query(model)
      for filter in filters:
          match filter.op:
              case "gt":
                  query = query.filter(getattr(model, filter.key) > filter.value)

              case "lt":
                  query = query.filter(getattr(model, filter.key) < filter.value)

              case "eq":
                  query = query.filter(getattr(model, filter.key) == filter.value)

              case "in":
                  query = query.filter(getattr(model, filter.key).in_(filter.value))

      if options:
        mapper = model.__mapper__
        relationships = []

        for prop in mapper.relationships:
            rel = prop
            relationships.append({
                'property': prop,
                'direction': 'one-to-many' if rel.direction.name == 'ONETOMANY' else 'many-to-one',
                'target': rel.mapper.class_,
                'back_populates': rel.back_populates
            })
            rel = relationships[-1]
            
            query = query.options(joinedload(getattr(model, str(prop).split(".")[1])))

      return query

def get_db():
  db = SessionLocal()

  try:
    yield db
  finally:
    db.close()


def using_db(func):
  def wrapper(*args, **kwargs):
    db = SessionLocal()
    result = None
    try:
      setattr(db, "build_filters", types.MethodType(build_filters, db))
      result = func(args[0], db, *args[1:], **kwargs)
    finally:
      db.close()
    return result
  return wrapper


def apply_using_db():
    def class_decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                sig = inspect.signature(attr_value)
                params = list(sig.parameters.values())

                if params[0].name == "self" and attr_name != "__init__" and attr_name != "get_navigation_properties":
                  print("dsdsdsldskdsmlkdmsl")
                  setattr(cls, attr_name, using_db(attr_value))

        return cls
    return class_decorator