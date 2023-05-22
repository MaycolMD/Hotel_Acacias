import datetime

class Paro:
    def __init__(self, inicio, fin, contexto):
        self.inicio = inicio.strftime('%Y-%m-%d')
        self.fin = fin.strftime('%Y-%m-%d')
        self.contexto = contexto
