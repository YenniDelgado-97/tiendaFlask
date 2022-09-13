from ast import AugStore
from .entidades.autor import autor
from .entidades.comic import comic


class modelocomic():
    
    @classmethod
    def listar_comics(self, db):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT com.isbn,com.titulo,com.anoedicion,com.precio,
            aut.apellidos,aut.nombres
            FROM comic com JOIN autor aut on com.autor_id= aut.id
            ORDER BY com.titulo ASC"""
            
            cursor.execute(sql)
            data= cursor.fetchall()
            comics=[]
            for row in data:
                aut= autor(0,row[4],row[5])
                com=comic(row[0], row[1], aut,row[2],row[3])
                comics.append(com)
            return comics

        except Exception as ex:
            raise Exception(ex)