# Funciones.py

def calcular_suma_votos(votos: list) -> int:
    """
    Calcula de forma artesanal la suma total de los votos del vector.
    Recibe: Una lista con los votos de los partidos.
    Devuelve: Un entero con el total acumulado.
    """
    total = 0
    for i in range(len(votos)):
        total += votos[i]
    return total

def calcular_promedio_votos(votos: list) -> float:
    """
    Calcula el promedio de votos por partido político.
    Recibe: Una lista con los votos.
    Devuelve: Un flotante con el promedio general.
    """
    total = calcular_suma_votos(votos)
    if len(votos) == 0:
        return 0.0
    return total / len(votos)

def realizar_carga_secuencial(cantidad_partidos: int) -> list:
    """
    Se encarga de iterar y pedir los votos de cada partido usando el módulo Inputs.
    Recibe: La cantidad de partidos a cargar (ej: 5).
    Devuelve: Una lista con los votos cargados de forma secuencial.
    """
    import Inputs
    lista_votos = []
    for i in range(cantidad_partidos):
        partido_votos = Inputs.pedir_votos_partido(f"Ingrese votos para el Partido {i + 1}: ")
        lista_votos.append(partido_votos)
    return lista_votos

def obtener_partidos_menos_porcentaje(votos: list, porcentaje_limite: float) -> list:
    """
    Filtra los índices de los partidos cuyo porcentaje de votos sea menor al límite.
    Recibe: La lista de votos y el porcentaje límite (10, 15 o 20).
    Devuelve: Una lista de índices de los partidos que cumplen la condición.
    """
    total_general = calcular_suma_votos(votos)
    indices_encontrados = []
    if total_general == 0:
        return indices_encontrados
        
    for i in range(len(votos)):
        porcentaje_partido = (votos[i] / total_general) * 100
        if porcentaje_partido < porcentaje_limite:
            indices_encontrados.append(i)
    return indices_encontrados

def obtener_partidos_mas_votos(votos: list, minimo_votos: float) -> list:
    """
    Filtra los índices de los partidos que superen una cantidad mínima de votos o un promedio.
    Recibe: La lista de votos y el valor mínimo a superar.
    Devuelve: Una lista de índices correspondientes.
    """
    indices_encontrados = []
    for i in range(len(votos)):
        if votos[i] > minimo_votos:
            indices_encontrados.append(i)
    return indices_encontrados

def obtener_partidos_menos_votados_con_empate(votos: list) -> list:
    """
    Busca el menor valor de votos y encuentra todos los partidos que tengan esa cantidad (contempla empates).
    Recibe: La lista de votos.
    Devuelve: Una lista de índices de los partidos menos votados.
    """
    if len(votos) == 0:
        return []
    
    valor_minimo = votos[0]
    for i in range(1, len(votos)):
        if votos[i] < valor_minimo:
            valor_minimo = votos[i]
            
    indices_minimos = []
    for i in range(len(votos)):
        if votos[i] == valor_minimo:
            indices_minimos.append(i)
    return indices_minimos

def ordenar_nombres_alfabeticamente(lista_nombres: list) -> list:
    """
    Ordena una lista de cadenas de caracteres mediante el algoritmo Bubble Sort de forma artesanal.
    Recibe: Una lista de nombres desordenada.
    Devuelve: Una nueva lista ordenada de la A a la Z.
    """
    lista_copia = lista_nombres.copy()
    n = len(lista_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                aux = lista_copia[j]
                lista_copia[j] = lista_copia[j + 1]
                lista_copia[j + 1] = aux
    return lista_copia