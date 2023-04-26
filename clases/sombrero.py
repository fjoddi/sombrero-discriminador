import random
from datetime import datetime

class Sombrero:
    def __init__(self, lista, semilla):
        self.lista = lista
        self.semilla = semilla
        self.excluidos = []

    def seleccionar_perdedores(self):
        random.seed(self.semilla)
        perdedores = []
        while len(perdedores) < 4:
            perdedor_index = int(random.random() * len(self.lista))
            perdedor = self.lista.pop(perdedor_index)
            perdedores.append(perdedor)
        self.excluidos = [elem for elem in self.lista if elem not in perdedores]
        return perdedores