import peewee
from utils.db import db

class Ubicacion(peewee.Model):
    key_ubicacion = peewee.UUIDField(primary_key=True, index=True)
    key_cp_ubicacion = peewee.CharField(unique=True, index=True)
    pais = peewee.CharField()
    estado = peewee.CharField()
    ciudad = peewee.CharField()
    creation_time = peewee.DateTimeField()
    modification_time = peewee.DateTimeField()

    def getUbicacionByKey():
        print("Método para obtener usuario")
    def getUbicacionByCP():
        print("Método para obtener usuario")

    class Meta:
        database = db
        table_name = 'Ubicacion'