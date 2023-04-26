import os
import json
from datetime import datetime

class ArchivoJson:
    JSON_FILENAME = "log\excluidos.json"
    
    def leer(self):
        if os.path.exists(self.JSON_FILENAME):
            with open(self.JSON_FILENAME) as f:
                return json.load(f)
        else:
            return {}

    def escribir(self, diccionario):
        with open(self.JSON_FILENAME, 'w') as f:
            json.dump(diccionario, f)