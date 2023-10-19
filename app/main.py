# archivo main.py
from fastapi import FastAPI
from pydantic import BaseModel
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
#Leer los parámetros de .env
load_dotenv()
class Settings(BaseSettings):
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": "Hello World"}