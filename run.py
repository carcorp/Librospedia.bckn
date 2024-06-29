#De la libreria de Flask importame la clase flask ??  
from flask import Flask
#Le coloco * para no tener que nombrar todas las rutas
from app.views import *
#Llamo a funcion init_app del archivo database
from app.database import init_app
#CORS
from flask_cors import CORS, cross_origin


#Inicializacion de la aplicacion con flask 
#Variable especial que se establece automaticamente cuando el archivo esta siendo ejecutado y puede tomar varios valores  
app = Flask (__name__)

init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app, supports_credentials=True)

#Registrar una ruta asociada a una vista 
#SI no coloco el metodo va a ser por default un GET
app.route('/api/books/', methods=['GET'])(get_all_books)
app.route('/api/books/', methods=['POST'])(create_book)
app.route('/api/books/<int:book_id>', methods=['GET'])(get_book)
app.route('/api/books/<int:book_id>', methods=['PUT'])(update_book)
app.route('/api/books/<int:book_id>', methods=['DELETE'])(delete_book)
cross_origin(supports_credentials=True)

#Está condicion va a tomar la variable name el valor main cuando se ejecute el archivo de python 
if __name__ == '__main__':
    #Levanta el servidor de desarrollo de flask 
    app.run(debug=True)



