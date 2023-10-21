# archivo main.py
import hashlib
import uuid
import peewee
from model.Usuario_model import Usuario as UsuarioModel
from model.Datos_Usuario_model import DatosUsuario as DatosUsuarioModel
from fastapi import FastAPI
import time
from datetime import datetime  
from pydantic import BaseModel
app = FastAPI()

class Usuario_Modelo(BaseModel):
    username: str
    secret: str
    nombre: str | None = None
    apellido: str | None = None
    edad: int | None = None
    email: str
    ciudad: str | None = None

@app.get("/")
def read_root():
    return {"Este es un mensaje": "Hello World, replicando en tiempo real"}
#Creación de usuarios nuevos. Recibe como parámetros una función y devuelve 1 si todo salio bien
@app.post("/crearNuevoUsuario/{model_usuario}")
def create_item(usuario_modelo: Usuario_Modelo):
    if(usuario_modelo):
        uuid_gen = uuid.uuid5(uuid.NAMESPACE_DNS, usuario_modelo.username)
        try:
            chk_username = UsuarioModel.getUserbyUsername(arg = usuario_modelo.username)
            if(chk_username) == None: #Verificar si el correo ya está en uso
                try:
                    chk_email = DatosUsuarioModel.getUserbyEmail(arg = usuario_modelo.email)
                    if(chk_email) == None: #Verificar si ya está creado
                        try:
                            timestamp_now = datetime.fromtimestamp(time.time())
                            usuarioNuevo = UsuarioModel.create(pk_uuid = uuid_gen, 
                                           username = usuario_modelo.username, 
                                           secret = hashlib.sha256((usuario_modelo.secret).encode()), 
                                           creation_time = timestamp_now,
                                           modification_time = timestamp_now)
                            datosUsuarioNuevo = DatosUsuarioModel.create(fk_uuid_usuario = uuid_gen,
                                                         nombre = usuario_modelo.nombre,
                                                         apellido = usuario_modelo.apellido,
                                                         edad = usuario_modelo.edad,
                                                         email = usuario_modelo.email
                                                         )
                        except:
                            return{"key" : 5002, "message" : "Error interno"}
                        else:
                            return{"key" : 1, "message" : "Registro creado con éxito"}
                except:
                    return{"key" : 5003, "message" : "Error interno"}
                else:
                    return{"key" : 1, "message" : "El correo está en uso"}
        except: #Si no se ha creado, procede a checar si ninguno de los datos cruciales se repiten
            return{"key" : 5001, "message" : "Error interno"}
        return{"key" : 1, "message" : "El username está en uso"}

@app.post("/modificarDatosUsuario/{modelo}")
def modify_item(du_modelo: Usuario_Modelo):
    if(du_modelo):
        uuid_gen = uuid.uuid5(uuid.NAMESPACE_DNS, du_modelo.username)
        try:
            chk_username = UsuarioModel.select().join(
                DatosUsuarioModel, on=(
                    UsuarioModel.pk_uuid == DatosUsuarioModel.fk_uuid_usuario)).where(
                        UsuarioModel.username == du_modelo.username)
            if chk_username:
                for x, y in du_modelo:
                    print("key: ", x)
                    print("value: ", y)
        except:
            return{5005}
@app.post("/consultarUsuario/{username}")
def getUser(nomUsuario : str):
    Usuario = UsuarioModel.getUserbyUsername(nom_Usuario = nomUsuario)
    if Usuario.username == nomUsuario:
        return 1 #Si el usuario ya existe, retorna 1
    else:
        return 0 #Si el usuario no existe todavía, retorna 0
