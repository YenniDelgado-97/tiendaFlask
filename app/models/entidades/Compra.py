from datetime import datetime

import datetime


class Compra():

    def __init__(self, uuid, comic, usuario, fecha=None):
        self.uuid = uuid
        self.comic = comic
        self.usuario = usuario
        self.fecha = fecha

    def formatted_date(self):
        return datetime.datetime.strftime(self.fecha,'%d/%m/%Y - %H:%M:%S')