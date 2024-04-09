from typing import TypeVar,Generic, Type, Optional, Any, List

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models.base_model import BaseModel as Base



TableModel=TypeVar("TableModel",bound=Base)

CreateModel=TypeVar("CreateModel",bound=BaseModel)

UpdateModel = TypeVar("UpdateModel",bound=BaseModel)


class CRUDBase(Generic[TableModel,CreateModel, UpdateModel]):
    
    def __init__(self,model: Type[TableModel]) -> None:
        self.model = model

    
    def __get_query_instance(self, db: Session,*, id: Optional[int] = None, filters: Optional[List[Any]] = None, skip: Optional[int] = None, limit: Optional[int] = None):
        query = db.query(self.model)
        
        if id is not None:
            query = query.filter(self.model.id == id)

        if filters is not None:
            for _filters in filters:
                query = query.filter(_filters)

        if skip: 
            query = query.offset(skip)

        if limit: 
            query = query.limit(limit)

        return query

    def get_all_record(self, db: Session,*, id: Optional[int] =None, filters: Optional[List[Any]] = None, skip: Optional[int] = None, limit: Optional[int] = None):
        return self.__get_query_instance(db, id=id, filters=filters, skip=skip, limit=limit).all()
    
    def get_record(self, db: Session,*, id: Optional[int] = None, filters: Optional[List[Any]] = None, skip: Optional[int] = None, limit: Optional[int] = None):
        return self.__get_query_instance(db, id=id, filters=filters, skip=skip, limit=limit).first()
    
    def get_count(self, db: Session ):
        return db.query(self.model).count()
    
    def create(self, db: Session, obj: CreateModel ):
        
        row_data = jsonable_encoder(obj)


        in_schema_form = self.model( **row_data )
        db.add(in_schema_form)  

        db.commit()
        db.refresh(in_schema_form)
        
        return in_schema_form
    
    def updates(self,db:Session,obj:UpdateModel):
        model_instance = db.query(self.model).filter(self.model.id == obj.id)
        model_instance.update(dict(obj))
        db.commit()
        return model_instance.first()




