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
