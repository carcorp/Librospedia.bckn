#agrego las clases que se van a asociar a la capa de datos de mi base de datos 

from app.database import get_db

class Book:

    #constructor
    def __init__(self,id_book=None,title=None, language=None, ranking=None, video_url=None, cover=None, author=None):
        self.id_book = id_book
        self.title = title
        self.language = language
        self.ranking = ranking
        self.video_url = video_url
        self.cover = cover
        self.author = author

    #Otro metodo que está armando
    #Proceso de conversion de un objeto de la clase libro en un diccionario
    def serialize(self): #Metodo de la instancia
        return {
            'id_book': self.id_book,
            'title': self.title,
            'language': self.language,
            'ranking': self.ranking,
            'video_url': self.video_url,
            'cover': self.cover,
            'author':self.author,
        }

    #Otro metodo +
    @staticmethod #Llama de lo generico a lo especifico 
    def get_all():
        #Logica que se encarga de buscar en la base todas las Libros
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        #Obtengo resultados 
        rows = cursor.fetchall()
        books = [Book(id_book=row[0],title=row[1], language=row[2], ranking=row[3], video_url=row[4], cover=row[5], author= row[6]) for row in rows]
        #Cerramos el cursor 
        cursor.close()
        return books
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_book:
            #Forma de poder insertar ("" 3 comillas string) elementos o variables dentro de una cadena
            cursor.execute("""
                UPDATE books SET title = %s, language = %s, ranking = %s, video_url = %s, cover = %s, author = %s
                WHERE id_book = %s
            """, (self.title, self.language, self.ranking, self.video_url, self.cover, self.author, self.id_book))
        else:
            cursor.execute("""
                INSERT INTO books (title, language, ranking, video_url,cover, author) VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.title, self.language, self.ranking, self.video_url, self.cover, self.author))
            #voy a obtener el último id generado
            self.id_book = cursor.lastrowid
        db.commit() #poder confirmar la accion correspondiente
        cursor.close()

    @staticmethod
    def get_by_id(book_id):
        #Logica que se encarga de buscar en la base todas las Libros
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books WHERE id_book = %s",(book_id,))
        #Obtengo resultados 
        row = cursor.fetchone()
        #Cerramos el cursor 
        cursor.close()
        if row:
            return Book(id_book=row[0],title=row[1], language=row[2], ranking=row[3], video_url=row[4], cover=row[5], author=row[6])
        return None
    
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM books WHERE id_book = %s", (self.id_book,))
        db.commit()
        cursor.close()
