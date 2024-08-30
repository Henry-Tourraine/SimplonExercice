from sqlalchemy.orm import Session
from BDD.Context import apply_using_db
from DTO.PropertiesUpdate import PropUpdate
from sqlalchemy.orm import joinedload
from BDD.utils import Filter
from sqlalchemy import inspect


@apply_using_db()
class BaseRepository():
    def __init__(self, model):
        self.Model = model
        

    def create(self, db: Session, element):
        db.add(element)
        db.commit()
        db.refresh(element)
        return element


    def get_one_by(self, db: Session, key: str, value):
        return db.query(self.Model).filter(getattr(self.Model, key) == value).first()

    
    def get_many_by(self, db: Session, key: str, value, options: bool = False):
        return db.build_filters(self.Model, [Filter(key, "eq", value)], options).all()


    def get_many_by_many(self, db: Session, filters: list[Filter], options=False):
        return db.build_filters(self.Model, filters, options).all()
    

    def get_many_by_many_ids(self, db: Session, ids: list):
        return self.get_many_by_many([Filter("id", "in", ids)])
    
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(self.Model).offset(skip).limit(limit).all()

    
    def update(self, db: Session, id: int, props=list[PropUpdate]):
        element = db.query(self.Model).filter(self.Model.id == id).first()
        if element:
            for prop in props:
                att = getattr(self.Model, prop.key)
                if att:
                    setattr(element, prop.key, prop.value)
           
            db.commit()
            db.refresh(element)
        return element


    
    def delete(self, db: Session, id: int):
        element = db.query(self.Model).filter(self.Model.id == id).first()
        if element:
            db.delete(element)
            db.commit()
        return element