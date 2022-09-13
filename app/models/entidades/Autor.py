class Autor():

    def __init__(self, id, apellidos, nombre):
        self.id = id
        self.apellidos = apellidos
        self.nombre = nombre

    def nombre_completo(self):
        return "{0}, {1}".format(self.apellidos, self.nombre)
