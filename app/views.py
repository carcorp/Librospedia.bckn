#defino todas  las funciones y vistas del corazon de la aplicacion, que quiero que haga

from flask import jsonify, request
from app.models import Book

#funcion q trae flask en libreria y que permite convertir en formato json - listas y diccionarios de python
#indicar también el codigo de la respuesta 


def get_all_books():
    books = Book.get_all()
    return jsonify([book.serialize() for book in books])

def get_book(book_id):
    book = Book.get_by_id(book_id)
    if not book:
        return jsonify({'message':'Book not found'}),404
    return jsonify(book.serialize())

def create_book():
    #Toma los datos ingresados en el crud en los distintos campos que viajaron en ese formato y conertirlos en un diccionario de python
    #Con esto obtengo los datos enviados en formato json - convierte en un diccionario de python
    data = request.json
    #Proceso de validacion, no nec para el tpo pero se puede implementar
    # if(data['title']==''):
    #     return jsonify({'message':"El campo titulo es obligatorio"}),500
    new_book = Book(None,data['title'],data['language'],data['ranking'],data['video_url'],data['cover'],data['author'])
    new_book.save()
    response = {'message':'Book successfully created' }
    return jsonify(response),201

def update_book(book_id):
    book = Book.get_by_id(book_id)
    if not book:
        return jsonify({'message':'Book not found'}),404
    data = request.json
    book.title = data['title']
    book.language = data ['language']
    book.ranking = data ['ranking']
    book.video_url = data ['video_url']
    book.cover = data ['cover']
    book.author = data ['author']
    book.save()
    return jsonify({'message':'Book updated successfully'})

def delete_book(book_id):
    book = Book.get_by_id(book_id)
    if not book:
        return jsonify({'message':'Book not found'}),404
    book.delete()
    return jsonify({'message':'Book deleted successfully'})
