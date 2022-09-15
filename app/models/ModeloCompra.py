from .entidades.Compra import Compra
from .entidades.Comic import Comic


class ModeloCompra():

    @classmethod
    def registrar_compra(self, db, compra):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO compra (uuid, comic_isbn, usuario_id) 
                VALUES (uuid(), '{0}',{1}) """.format(compra.comic.isbn, compra.usuario.id)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def listar_compras_usuario(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT COM.fecha, CO.isbn, CO.titulo, CO.precio
                    FROM compra COM JOIN comic CO ON COM.comic_isbn = CO.isbn
                    WHERE COM.usuario_id = {0}""".format(usuario.id)
            cursor.execute(sql)
            data = cursor.fetchall()
            compras = []
            for row in data:
                co = Comic(row[1], row[2], None, None, row[3])
                com = Compra(None, co, usuario, row[0])
                compras.append(com)
            return compras

        except Exception as ex:
            raise Exception(ex)
