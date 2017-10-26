# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

import sqlalchemy
import sqlalchemy.dialects.mysql

class Boolean(sqlalchemy.Column):
    
    def __init__(self):
        sqlalchemy.Column.__init__(self, sqlalchemy.Boolean)

class Integer(sqlalchemy.Column):
    
    def __init__(self):
        sqlalchemy.Column.__init__(self, sqlalchemy.dialects.mysql.INTEGER)

class Float(sqlalchemy.Column):
    
    def __init__(self):
        sqlalchemy.Column.__init__(self, sqlalchemy.Float)

class Time(sqlalchemy.Column):
    
    def __init__(self):
        sqlalchemy.Column.__init__(self, sqlalchemy.Time)

class String(sqlalchemy.Column):
    
    def __init__(self, length=None):
        sqlalchemy.Column.__init__(self, sqlalchemy.String(length))

class Text(sqlalchemy.Column):
    
    def __init__(self):
        sqlalchemy.Column.__init__(self, sqlalchemy.Text)
