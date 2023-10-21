import peewee
from utils.db import db
from model.Usuario_model import Usuario

class DatosUsuario(peewee.Model):
    fk_uuid_usuario = peewee.ForeignKeyField(Usuario, backref='pk_uuid')
    pk_historico_consulta = peewee.IntegerField(primary_key=True, index=True)
    fk_key_ubicacion = peewee.CharField(foreign_key=True, index=True)
    clima = peewee.CharField()
    presion = peewee.IntegerField()
    humedad = peewee.IntegerField()
    velviento = peewee.IntegerField()
    temperatura_actual = peewee.IntegerField()
    temperatura_max = peewee.IntegerField()
    temperatura_min = peewee.IntegerField()
    creation_time = peewee.DateTimeField()
    modification_time = peewee.DateTimeField()

    def getHistoricoByUuid():
        print("Método para obtener usuario")
    def getHistoricoByUuidId():
        print("Método para obtener usuario")

    class Meta:
        database = db
        table_name = 'Historico_Consulta'