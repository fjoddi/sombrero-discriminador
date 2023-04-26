import json

class Estadisticas:
    def __init__(self, archivo):
        self.archivo = archivo
        self.stats = {}

    def calcular(self):
        # Cargamos el archivo JSON
        with open(self.archivo, 'r') as f:
            data = json.load(f)

        # Creamos un diccionario vacío para almacenar las estadísticas
        self.stats = {}

        # Iteramos sobre los valores del diccionario
        for valores in data.values():
            # Iteramos sobre los nombres en cada valor
            for nombre in valores:
                # Si el nombre ya existe en las estadísticas, aumentamos su contador en 1
                if nombre in self.stats:
                    self.stats[nombre] += 1
                # Si el nombre no existe en las estadísticas, lo agregamos con contador en 1
                else:
                    self.stats[nombre] = 1

    def imprimir(self):
        # Imprimimos las estadísticas
        for nombre, cantidad in self.stats.items():
            print(f'{nombre}: {cantidad} veces Azkabaneado')
