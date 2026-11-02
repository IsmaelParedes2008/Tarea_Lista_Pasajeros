# =====================================================================
#  ejercicio.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#  Aquí van TODOS los ejercicios del módulo 📋 Listas de la guía:
#     • 3 ejercicios DESARROLLADOS (taller paso a paso)  -> T1, T2, T3
#     • 5 ejercicios PROPUESTOS (solución oculta)         -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que:
#     1) imprime su enunciado corto,
#     2) usa datos fijos de prueba (los indicados en cada función),
#     3) muestra el resultado.
#
#  REGLA: en cada ejercicio resuelve con DOS versiones cuando se indique:
#     ✋ MANUAL (bucles, patrones del módulo 0)  y  🐍 PYTHON (built-ins
#     y comprensiones). Imprime ambas para comparar.
#  Cuando termines una función, BORRA la línea "pass".
# =====================================================================

# ============================ DESARROLLADOS ==========================

def ejercicio_t1():
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero

    print("T1 — CRUD de pasajeros con clase Pasajero + list")
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana", "0912345678", 28))
    lista.añadir(Pasajero("Luis", "0987654321", 35))

    print("\n-- Listar --")
    lista.listar()

    print("\n-- Buscar cédula 0912345678 --")
    pos = lista.buscar("0912345678")
    print(f"Encontrado en [{pos}]: {lista.pasajeros[pos]}")

    print("\n-- Modificar Ana -> Anita, 29 --")
    lista.modificar("0912345678", "Anita", 29)
    lista.listar()

    print("\n-- Eliminar cédula 0923456789 (Diana) --")
    lista.eliminar_por_valor("0923456789")
    lista.listar()

    print("\n-- Ordenar por NOMBRE (sort con lambda) --")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    lista.listar()


def ejercicio_t2():
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]
    print("T2 — Estadísticas de una lista de notas")

    # ✋ MANUAL: un solo for con acumulador, campeón y contador
    suma = 0
    maxima = notas[0]
    minima = notas[0]
    mejor = nombres[0]
    aprobados = 0
    for i in range(len(notas)):
        suma = suma + notas[i]
        if notas[i] > maxima:
            maxima = notas[i]
            mejor = nombres[i]
        if notas[i] < minima:
            minima = notas[i]
        if notas[i] >= 7:
            aprobados = aprobados + 1
    promedio = suma / len(notas)
    print(f"✋ Promedio {promedio:.2f} · Máx {maxima} ({mejor}) · Mín {minima} · Aprobados {aprobados} de {len(notas)}")

    # 🐍 PYTHON: built-ins y comprensión
    maxima_p = max(notas)
    mejor_p = nombres[notas.index(maxima_p)]
    aprobados_p = [n for n in notas if n >= 7]
    print(f"🐍 Promedio {sum(notas) / len(notas):.2f} · Máx {maxima_p} ({mejor_p}) · Mín {min(notas)} · Aprobados {len(aprobados_p)} de {len(notas)}")


def ejercicio_t3():
    datos = [5, 2, 8, 1, 9, 3, 7]
    print("T3 — Ordenar una lista (bubble sort)")

    # ✋ MANUAL: burbuja con bandera hubo_swap sobre una COPIA
    copia = datos[:]
    n = len(copia)
    for vuelta in range(n - 1):
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if copia[i] > copia[i + 1]:
                aux = copia[i]
                copia[i] = copia[i + 1]
                copia[i + 1] = aux
                hubo_swap = True
        if not hubo_swap:
            break
    print("✋", copia)

    # 🐍 PYTHON
    print("🐍", sorted(datos))
    desc = datos[:]
    desc.sort(reverse=True)
    print("🐍 descendente:", desc)

    # Extra: palabras ordenadas por longitud
    palabras = ["python", "a", "código", "el"]
    print("Extra (key=len):", sorted(palabras, key=len))


# ============================= PROPUESTOS ============================

def ejercicio_p1():
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3
    print("P1 — Contar apariciones de un valor")

    # ✋ MANUAL: patrón contador
    contador = 0
    for x in lista:
        if x == v:
            contador = contador + 1
    print(f"✋ {v} aparece {contador} veces")

    # 🐍 PYTHON
    print(f"🐍 {v} aparece {lista.count(v)} veces")

    # 🧩 COMPRENSIÓN
    print(f"🧩 {v} aparece {len([x for x in lista if x == v])} veces")


def ejercicio_p2():
    lista = [1, 2, 3, 4, 5]
    print("P2 — Invertir una lista SIN lista.reverse()")

    # ✋ MANUAL
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print("✋", invertida)

    # 🐍 PYTHON
    print("🐍", lista[::-1])
    print("🐍", list(reversed(lista)))

    # 🧩 COMPRENSIÓN
    print("🧩", [lista[i] for i in range(len(lista) - 1, -1, -1)])


def ejercicio_p3():
    nums = [1, 3, 2, 3, 4, 1, 5, 2]
    print("P3 — Números únicos manteniendo el orden")

    # ✋ MANUAL
    unicos = []
    for n in nums:
        if n not in unicos:
            unicos.append(n)
    print("✋", unicos)

    # 🐍 PYTHON
    print("🐍", list(dict.fromkeys(nums)))
    # list(set(nums)) NO garantiza el orden: un set no tiene orden propio.
    # dict.fromkeys sí lo conserva, porque un dict guarda el orden de inserción.


def ejercicio_p4():
    nums = [5, 2, 9, 7, 9, 3, 8]
    print("P4 — Segundo mayor (sin ordenar toda la lista)")

    # ✋ MANUAL: dos campeones en un solo recorrido
    mayor = nums[0]
    segundo = None
    for n in nums:
        if n > mayor:
            segundo = mayor
            mayor = n
        elif n != mayor and (segundo is None or n > segundo):
            segundo = n
    print(f"✋ Mayor {mayor} · Segundo {segundo}")

    # 🐍 PYTHON (para comprobar)
    ordenados = sorted(set(nums))
    print(f"🐍 Mayor {ordenados[-1]} · Segundo {ordenados[-2]}")


def ejercicio_p5():
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    print("P5 — Fusionar dos listas ordenadas (sin sort)")

    # ✋ MANUAL: dos índices comparando cabezas
    resultado = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i = i + 1
        else:
            resultado.append(b[j])
            j = j + 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    print("✋", resultado)

    # 🐍 PYTHON (para comprobar)
    print("🐍", sorted(a + b))


# ============================== CATÁLOGO =============================
EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    while True:
        taller = [e for e in EJERCICIOS if e[2] == "taller"]
        propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]

        print("\n--- DESARROLLADOS (taller) ---")
        for e in taller:
            print(f"  {e[0]}. {e[1]}")
        print("--- PROPUESTOS ---")
        for e in propuestos:
            print(f"  {e[0]}. {e[1]}")
        print("  0.  Volver")

        codigo = input("Código: ").strip().upper()
        if codigo == "0":
            break

        encontrados = [e for e in EJERCICIOS if e[0] == codigo]
        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("Código no válido")