# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __sql_proto__:
    
    def __init__(self):
        self.smaker = sessionmaker(bind=self.engine)
        self._session = None
    
    def session(self):
        if self._session == None: self._session = self.smaker()
        return self._session
    
    def refresh(self):
        if self._session != None:
            try: self._session.commit()
            except: pass
        self._session = self.smaker()
        return self._session

class Memory(__sql_proto__):
        
    def __init__(self):
        self.proto = 'sqlite:///:memory:'
        self.engine = create_engine(self.proto)
        self.engine.execute('select 1').scalar()
        __sql_proto__.__init__(self)

class File(__sql_proto__):
    
    def __init__(self):
        _, name = pmd()
        self.proto = 'sqlite:///%s/%s.db' % (ENV.DIR.SVC, name)
        self.engine = create_engine(self.proto)
        self.engine.execute('select 1').scalar()
        __sql_proto__.__init__(self)
    
class Mysql(__sql_proto__):
    
    def __init__(self, host, username, password, root_name=''):
        _, name = pmd()
        name = name.replace('.', '_')
        if root_name: name = '%s_%s' % (root_name, name)
        self.proto = 'mysql://%s:%s@%s' % (username, password, host)
        self.engine = create_engine(self.proto)
        self.engine.execute('select 1').scalar()
        self.engine.execute("CREATE DATABASE IF NOT EXISTS %s CHARACTER SET utf8;" % name)
        self.engine.execute("use %s;" % name)
        __sql_proto__.__init__(self)
