import peewee
from utils.db import db
from model.Usuario_model import Usuario
from model.Ubicacion_model import Ubicacion

class DatosUsuario(peewee.Model):
    fk_uuid_usuario = peewee.UUIDField(index=True)
    fk_usuario = peewee.ForeignKeyField(Usuario, field=Usuario.pk_uuid, constraint_name="fk_uuid_usuario")
    nombre = peewee.CharField(null=True)
    apellido = peewee.CharField(null=True)
    edad = peewee.IntegerField(null=True)
    fk_key_ubicacion = peewee.CharField(default = None, index = True)
    fk_Ubicacion = peewee.ForeignKeyField(Ubicacion, backref="pk_key_ubicacion")
    email = peewee.CharField(index=True)
    
    def getUserbyEmail(arg : str):
        get_query = Usuario.get_or_none(Usuario.username == arg)
        return get_query

    class Meta:
        database = db
        table_name = 'Datos_Usuario'
        primary_key = False