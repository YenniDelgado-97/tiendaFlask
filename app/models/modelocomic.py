from ast import AugStore
from .entidades.autor import autor
from .entidades.comic import comic


class modelocomic():

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
                aut = autor(0, row[4], row[5])
                com = comic(row[0], row[1], aut, row[2], row[3])
                comics.append(com)
            return comics

        except Exception as ex:
            raise Exception(ex)
