from ast import AugStore
from .entidades.Autor import Autor
from .entidades.Comic import Comic


class ModeloComic():

    @classmethod
    def listar_comics(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT COM.isbn,COM.titulo,COM.anoedicion,COM.precio,
                AUT.apellidos,AUT.nombre
                FROM comic COM JOIN autor AUT ON COM.autor_id= AUT.id 
                ORDER BY COM.titulo ASC"""

            cursor.execute(sql)
            data = cursor.fetchall()
            comics = []
            for row in data:
                aut = Autor(0, row[4], row[5])
                com = Comic(row[0], row[1], aut, row[2], row[3])
                comics.append(com)
            return comics

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def listar_comics_vendidos(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT COM.comic_isbn, CO.titulo,CO.precio,
                        COUNT(COM.comic_isbn) AS Unidades_Vendidas
                        FROM compra COM JOIN comic CO ON COM.comic_isbn = CO.isbn
                        GROUP BY COM.comic_isbn ORDER BY 4 DESC, 2 ASC"""

            cursor.execute(sql)
            data = cursor.fetchall()
            comics = []
            for row in data:

                com = Comic(row[0], row[1], None, None, row[2])
                com.unidades_vendidas = int(row[3])
                comics.append(com)
            return comics

        except Exception as ex:
            raise Exception(ex)
