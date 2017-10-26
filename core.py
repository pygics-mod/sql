# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

import jzlib
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()

class Sql(jzlib.LifeCycle):
    
    def __init__(self, proto):
        self._sql_proto = proto
        self._sql_engine = proto.engine
        self._sql_session = proto.session
        
    def __release__(self):
        self.close()
    
    def close(self):
        self._sql_session.close_all()
        self._sql_engine.dispose()

class Model(Base):
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True)
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    @classmethod
    def get(cls, id):
        return cls.__db__._sql_session.query(cls).get(id)
    
    @classmethod
    def one(cls, *clause):
        result = cls.__db__._sql_session.query(cls)
        for c in clause: result = result.filter(c)
        try: return result.first()
        except: return None
    
    @classmethod
    def list(cls, *clause):
        result = cls.__db__._sql_session.query(cls)
        for c in clause: result = result.filter(c)
        return result
    
    @classmethod
    def count(cls, *clause):
        result = cls.__db__._sql_session.query(cls)
        for c in clause: result = result.filter(c)
        return result.count()
    
    def create(self):
        self.__class__.__db__._sql_session.add(self)
        self.__class__.__db__._sql_session.commit()
        return self
        
    def update(self, **keyval):
        for key, val in keyval.items(): self.__setattr__(key, val)
        self.__class__.__db__._sql_session.commit()
        return self
    
    def delete(self):
        self.__class__.__db__._sql_session.delete(self)
        self.__class__.__db__._sql_session.commit()
        return self

def model(sql):
    def wrapper(scheme):
        scheme.__db__ = sql
        scheme.__table__.create(sql._sql_engine, checkfirst=True)
        return scheme
    return wrapper