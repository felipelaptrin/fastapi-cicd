from api.config.db import db
from peewee import CharField, BooleanField, Model, AutoField


class User(Model):
    id = AutoField()
    first_name = CharField(50)
    last_name = CharField(50)
    email = CharField(50)
    is_active = BooleanField(50)
    
    class Meta:
        database = db
        table_name = 'user'
