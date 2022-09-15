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
