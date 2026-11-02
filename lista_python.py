# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero ahora usamos lo que Python
#  ya trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, next, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  ✅ OBLIGATORIO usar comprensiones de listas en (mínimo):
#       buscar · buscar_binaria · eliminar_por_valor (versión 2)
#       filtrar_mayores_de_edad · nombres_en_mayusculas
# =====================================================================

from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:

    def __init__(self):
        self.pasajeros = []               # list de Python: crece sola

    def añadir(self, pasajero):
        """Añade al final con append(), sin cédulas repetidas."""
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        if not self.pasajeros:
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    def longitud(self):
        # Lista 1: 1 línea · Lista 2: 1 línea
        return len(self.pasajeros)

    def insertar(self, posicion, pasajero):
        # Lista 1: 16 líneas · Lista 2: 8 líneas (6 de validación + 1 insert + 1 return)
        # ¿Python corre los elementos? SÍ. insert() mueve a la derecha todos los
        # que están después de la posición, igual que mi while, solo que no lo veo.
        # Por eso es O(n): en el peor caso (insertar al inicio) mueve los n elementos.
        if posicion < 0 or posicion > len(self.pasajeros):
            print("⚠ Posición no válida")
            return False
        if self.buscar(pasajero.cedula) != -1:
            print("⚠ Ya existe un pasajero con esa cédula")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, cedula):
        # Lista 1: 4 líneas · Lista 2: 4 líneas (1 es la comprensión)
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        if not posiciones:
            return -1
        return posiciones[0]

    def buscar_binaria(self, cedula):
        # Lista 1: 11 líneas · Lista 2: 5 líneas
        cedulas = [p.cedula for p in self.pasajeros]
        i = bisect_left(cedulas, cedula)
        if i < len(cedulas) and cedulas[i] == cedula:
            return i
        return -1

    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        # Lista 1: 7 líneas · Lista 2: 7 líneas (no hay atajo, es buscar + asignar)
        pos = self.buscar(cedula)
        if pos == -1:
            print("⚠ No existe un pasajero con esa cédula")
            return False
        self.pasajeros[pos].nombre = nuevo_nombre
        self.pasajeros[pos].edad = nueva_edad
        return True

    def eliminar_por_posicion(self, posicion):
        # Lista 1: 9 líneas · Lista 2: 4 líneas (3 de validación + pop)
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("⚠ Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, cedula):
        # Lista 1: 6 líneas · Lista 2: 3 líneas
        # FORMA 1 (remove), comentada para comparar:
        # pos = self.buscar(cedula)
        # if pos == -1:
        #     return False
        # self.pasajeros.remove(self.pasajeros[pos])
        # return True

        # FORMA 2 (comprensión), la activa:
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        # Lista 1: 7 líneas (burbuja) · Lista 2: 1 línea
        # ¿Qué hace key=? Le dice a sort() por QUÉ CAMPO comparar. Recibe una función
        # (la lambda) que saca la cédula de cada pasajero, y sort ordena por ese valor.
        # Sin key sale: TypeError: '<' not supported between instances of
        # 'Pasajero' and 'Pasajero' (Python no sabe cuál de los dos objetos es menor).
        self.pasajeros.sort(key=lambda p: p.cedula)

    def ordenar_desc(self):
        # Lista 1: 7 líneas · Lista 2: 1 línea
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    def reversar(self):
        # Lista 1: 8 líneas (dos punteros) · Lista 2: 1 línea
        self.pasajeros.reverse()

    def copiar(self):
        # Lista 1: 4 líneas · Lista 2: 3 líneas
        # Es una copia SUPERFICIAL: la lista es nueva (reversar la copia no toca el
        # original), pero los objetos Pasajero de adentro son los MISMOS en las dos.
        # Si modifico el nombre de un pasajero de la copia, el original también cambia,
        # porque los dos apuntan al mismo objeto.
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def filtrar_mayores_de_edad(self):
        # Lista 1: 5 líneas · Lista 2: 3 líneas (1 es la comprensión)
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    def nombres_en_mayusculas(self):
        # Lista 1: 4 líneas · Lista 2: 1 línea (la comprensión)
        return [p.nombre.upper() for p in self.pasajeros]