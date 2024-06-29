#va a contener todas las funciones o codigos que voy a utilizar para poder crear una conexion a la base de datos (verificar si existe o no y cerrarla)
import os 
import mysql.connector
from flask import g
from dotenv import load_dotenv

#Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'), 
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306)
} 

# Funcion para obtener la conexion a la base de datos 
def get_db():
    #Si'db' no esta en el contexto global de Flask 'g'
    if 'db' not in g:
        # Crear una nueva conexion a la base de datos y guardar
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
        # RETORNAR LA CONEXION A LA BASE DE DATO
        return g.db
#Funcion para cerrar la conexion a la base de datos
def close_db(e = None):
    # Extraer la conexion a la base de datos de 'g' y eliminarlo
    db = g.pop('db', None)
    # Si existe la conexion, cerrarlo
    if db is not None:
        db.close()

#Funcion para inicializar la aplicacion con el manejo de la ba:
def init_app(app):
    #Registrar 'close_db' para que se ejecute al final del con:
    app.teardown_appcontext(close_db)
    
    