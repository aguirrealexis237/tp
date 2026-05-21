# Funciones.py

def calcular_suma_votos(votos):
    total = 0
    for i in range(len(votos)):
        total += votos[i]
    return total

def calcular_promedio_votos(votos):
    total = calcular_suma_votos(votos)
    if len(votos) == 0:
        return 0.0
    return total / len(votos)

def obtener_partidos_menos_porcentaje(votos, porcentaje_limite):
    total_general = calcular_suma_votos(votos)
    indices_encontrados = []
    if total_general == 0:
        return indices_encontrados
        
    for i in range(len(votos)):
        porcentaje_partido = (votos[i] / total_general) * 100
        if porcentaje_partido < porcentaje_limite:
            indices_encontrados.append(i)
    return indices_encontrados

def obtener_partidos_mas_votos(votos, minimo_votos):
    indices_encontrados = []
    for i in range(len(votos)):
        if votos[i] > minimo_votos:
            indices_encontrados.append(i)
    return indices_encontrados

def obtener_partidos_menos_votados_con_empate(votos):
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

def ordenar_nombres_alfabeticamente(lista_nombres):
    lista_copia = lista_nombres.copy()
    n = len(lista_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                aux = lista_copia[j]
                lista_copia[j] = lista_copia[j + 1]
                lista_copia[j + 1] = aux
    return lista_copia