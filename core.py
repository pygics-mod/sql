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
        
    def __release__(self):
        self.close()
    
    def close(self):
        self._sql_proto.session.close_all()
        self._sql_proto.engine.dispose()

class Model(Base):
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True)
    
    @declared_attr
    def __tablename__(cls): return cls.__name__.lower()
    
    @classmethod
    def get(cls, id):
        try:
            try:
                session = cls.__db__._sql_proto.session()
                ret = session.query(cls).get(id)
                session.commit()
            except:
                session = cls.__db__._sql_proto.refresh()
                ret = session.query(cls).get(id)
                session.commit()
#             with session.begin(): return session.query(cls).get(id)
        except Exception as e:
            print type(e), str(e)
            ret = None
        return ret
    
    @classmethod
    def one(cls, *clause):
        try:
            try:
                session = cls.__db__._sql_proto.session()
                query = session.query(cls)
                for c in clause: query = query.filter(c)
                ret = query.first()
                session.commit()
            except:
                session = cls.__db__._sql_proto.refresh()
                query = session.query(cls)
                for c in clause: query = query.filter(c)
                ret = query.first()
                session.commit()
#             with session.begin():
#                 query = session.query(cls)
#                 for c in clause: query = query.filter(c)
#                 return query.first()
        except Exception as e:
            print type(e), str(e)
            ret = None
        return ret
    
    @classmethod
    def list(cls, *clause):
        try:
            try:
                session = cls.__db__._sql_proto.session()
                query = session.query(cls)
                for c in clause: query = query.filter(c)
                ret = query
                session.commit()
            except:
                session = cls.__db__._sql_proto.refresh()
                query = session.query(cls)
                for c in clause: query = query.filter(c)
                ret = query
                session.commit()
#             with session.begin():
#                 query = session.query(cls)
#                 for c in clause: query = query.filter(c)
#                 return query
        except Exception as e:
            print type(e), str(e)
            ret = []
        return ret
            
    @classmethod
    def count(cls, *clause):
        try:
            try:
                session = cls.__db__._sql_proto.session()
                query = session.query(cls)
                for c in clause: query = query.filter(c)
                ret = query.count()
                session.commit()
            except:
                session = cls.__db__._sql_proto.refresh()
                query = session.query(cls)
                for c in clause: query = query.filter(c)
                ret = query.count()
                session.commit()
#             with session.begin():
#                 query = session.query(cls)
#                 for c in clause: query = query.filter(c)
#                 return query.count()
        except Exception as e:
            print type(e), str(e)
            ret = 0
        return ret
    
    def create(self):
        try:
            try:
                session = self.__class__.__db__._sql_proto.session()
                session.add(self)
                session.commit()
            except:
                session = self.__class__.__db__._sql_proto.refresh()
                session.add(self)
                session.commit()
#             with session.begin(): session.add(self)
        except Exception as e: print type(e), str(e)
        return self
        
    def update(self, **keyval):
        try:
            try:
                session = self.__class__.__db__._sql_proto.session()
                for key, val in keyval.items(): self.__setattr__(key, val)
                session.commit()
            except:
                session = self.__class__.__db__._sql_proto.refresh()
                for key, val in keyval.items(): self.__setattr__(key, val)
                session.commit()
#             with session.begin():
#                 for key, val in keyval.items(): self.__setattr__(key, val)
        except Exception as e: print str(e)
        return self
    
    def delete(self):
        try:
            try:
                session = self.__class__.__db__._sql_proto.session()
                session.delete(self)
                session.commit()
            except:
                session = self.__class__.__db__._sql_proto.refresh()
                session.delete(self)
                session.commit()
#             with session.begin(): session.delete(self)
        except Exception as e: print str(e)
        return self

def model(sql):
    def wrapper(scheme):
        scheme.__db__ = sql
        scheme.__table__.create(sql._sql_proto.engine, checkfirst=True)
        return scheme
    return wrapper