from datetime import datetime
from clases.estadisticas import Estadisticas
from clases.operador_json import ArchivoJson
from clases.sombrero import Sombrero


class Programa:
    def __init__(self):
        self.archivo_json = ArchivoJson()

    def ejecutar(self):
        lista_texto = input("Ingresa las victimas separados por comas: ")
        lista = lista_texto.split(",")
        if len(lista) < 4:
            print("La lista debe tener al menos 4 victimas, el sombrero no labura por menos.")
            return

        semilla = input("Ingresa la semilla para el sorteo: ")
        semilla = int(semilla)

        sombrero = Sombrero(lista, semilla)
        perdedores = sombrero.seleccionar_perdedores()

        contenido_anterior = self.archivo_json.leer()
        fecha_ejecucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        contenido_actualizado = {fecha_ejecucion: sombrero.excluidos}
        contenido_anterior.update(contenido_actualizado)
        self.archivo_json.escribir(contenido_anterior)

        print("Damos inicio al Sombrero Discriminador")
        print("Lo alimentamos con:",semilla )

        if len(sombrero.excluidos) == 1:
            print("Este morocho pa'Azkaban -->",', '.join(sombrero.excluidos),"<-- Por puto")
        else:
            print("Todos estos morochos pa'Azkaban -->",', '.join(sombrero.excluidos),"<-- Por putos")

        estadisticas = Estadisticas('log/excluidos.json')
        estadisticas.calcular()
        estadisticas.imprimir()


if __name__ == '__main__':
    Programa = Programa()
    Programa.ejecutar()