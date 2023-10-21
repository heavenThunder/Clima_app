import peewee
from utils.db import db
import uuid

class Usuario(peewee.Model):
    pk_uuid = peewee.UUIDField(primary_key=True, index=True, unique=True)
    username = peewee.CharField(unique=True, index=True)
    secret = peewee.CharField()
    creation_time = peewee.DateTimeField()
    modification_time = peewee.DateTimeField()

    def getUserbyUsername(arg : str):
        get_query = Usuario.get_or_none(Usuario.username == arg)
        return get_query

    class Meta:
        database = db
        table_name = 'Usuario'