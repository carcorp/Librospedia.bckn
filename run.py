from flask import Flask
from app.views import *
from app.database import init_app

#inicializacion de la aplicacion con flask
#Variable especial que se establece automaicamente cuando el archivo está siendo ejecutado. 
app = Flask(__name__)

init_app(app)
#Registrar una ruta asociada a una vista
app.route('/api/books/', methods=['GET'])(get_all_books)
app.route('/api/books/', methods=['POST'])(create_book)
app.route('/api/books/<int:book_id>', methods=['GET'])(get_book)
app.route('/api/books/<int:book_id>', methods=['PUT'])(update_book)
app.route('/api/books/<int:book_id>', methods=['DELETE'])(delete_book)


if __name__ == '__main__':
    #Levnta el servidor de desarrollo Flask
    app.run(debug=True)
