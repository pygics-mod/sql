# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Memory:
        
    def __init__(self):
        self.proto = 'sqlite:///:memory:'
        self.engine = create_engine(self.proto)
        self.engine.execute('select 1').scalar()
        self.session = sessionmaker(bind=self.engine)()

class File:
    
    def __init__(self):
        _, name = pmd()
        self.proto = 'sqlite:///%s/%s.db' % (ENV.DIR.SVC, name)
        self.engine = create_engine(self.proto)
        self.engine.execute('select 1').scalar()
        self.session = sessionmaker(bind=self.engine)()

class Mysql:
    
    def __init__(self, host, username, password, root_name=''):
        _, name = pmd()
        name = name.replace('.', '_') 
        if root_name: name = '%s_%s' % (root_name, name)
        self.proto = 'mysql://%s:%s@%s' % (username, password, host)
        self.engine = create_engine(self.proto)
        self.engine.execute('select 1').scalar()
        self.engine.execute("CREATE DATABASE IF NOT EXISTS %s CHARACTER SET utf8;" % name)
        self.engine.execute("use %s;" % name)
        self.session = sessionmaker(bind=self.engine)()