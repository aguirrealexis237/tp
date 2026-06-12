# Prints.py
import Funciones

def mostrar_menu() -> None:
    """Muestra el panel de opciones principal del sistema."""
    print("\n==================================================")
    print("      SISTEMA DE ELECCIONES - UTN FRA             ")
    print("==================================================")
    print("1. Cargar votos (5 partidos)")
    print("2. Mostrar votos generales")
    print("3. Partidos con menos del 10% de votos")
    print("4. Partidos con menos del 15% de votos")
    print("5. Partidos con menos del 20% de votos")
    print("6. Partidos con más de 500 votos")
    print("7. Partidos con más de 1000 votos")
    print("8. Partidos por encima del promedio")
    print("9. Partido menos votado")
    print("10. Verificar segunda vuelta")
    print("11. Hardcodear vector (10 partidos)")
    print("12. Ordenar partidos políticos por nombre")
    print("0. Salir")
    print("==================================================")

def mostrar_error_no_cargado() -> None:
    """Muestra un mensaje de advertencia si se intenta consultar sin datos."""
    print("\n[!] Error: Debe cargar los votos (Opción 1 u 11) antes de realizar consultas.")

def mostrar_votos_generales(votos: list) -> None:
    """Muestra el listado general completo de los partidos calculando sus porcentajes."""
    total_votos = Funciones.calcular_suma_votos(votos)
    cant_partidos = len(votos)
    print(f"\n--- VOTOS GENERALES ---")
    print(f"Cantidad de partidos postulados: {cant_partidos}")
    print(f"Cantidad total de votos: {total_votos}\n")
    for i in range(cant_partidos):
        porcentaje = (votos[i] / total_votos) * 100
        print(f"Partido {i + 1}: {votos[i]} votos | Porcentaje: {porcentaje:.2f}%")

def mostrar_filtro_porcentajes(votos: list, limite: float) -> None:
    """Muestra los partidos que están por debajo del porcentaje límite indicado."""
    total_votos = Funciones.calcular_suma_votos(votos)
    indices = Funciones.obtener_partidos_menos_porcentaje(votos, limite)
    print(f"\n--- PARTIDOS CON MENOS DEL {limite}% DE VOTOS ---")
    
    if len(indices) == 0:
        print(f"[!] No hay partidos con menos del {limite}%.")
    else:
        porcentaje_acumulado = 0
        for idx in indices:
            porcentaje = (votos[idx] / total_votos) * 100
            print(f"Partido {idx + 1}: {votos[idx]} votos | Porcentaje: {porcentaje:.2f}%")
            porcentaje_acumulado += porcentaje
        print(f"Porcentaje acumulado de la búsqueda: {porcentaje_acumulado:.2f}%")

def mostrar_filtro_votos_minimos(votos: list, min_votos: float) -> None:
    """Muestra los partidos que superan un mínimo de votos y calcula los subtotales requeridos."""
    total_votos = Funciones.calcular_suma_votos(votos)
    indices = Funciones.obtener_partidos_mas_votos(votos, min_votos)
    print(f"\n--- PARTIDOS CON MÁS DE {min_votos} VOTOS ---")
    
    if len(indices) == 0:
        print(f"[!] No hay partidos con más de {min_votos} votos.")
    else:
        votos_subtotal = 0
        for idx in indices:
            porcentaje = (votos[idx] / total_votos) * 100
            print(f"Partido {idx + 1}: {votos[idx]} votos | Porcentaje: {porcentaje:.2f}%")
            votos_subtotal += votos[idx]
        
        promedio_subtotal = votos_subtotal / len(indices)
        print(f"\nSuma total de votos del filtro: {votos_subtotal}")
        print(f"Cantidad de partidos filtrados: {len(indices)}")
        print(f"Promedio de votos del filtro: {promedio_subtotal:.2f}")

def mostrar_por_encima_promedio(votos: list) -> None:
    """Muestra los partidos que superan el promedio general de votos."""
    total_votos = Funciones.calcular_suma_votos(votos)
    promedio_general = Funciones.calcular_promedio_votos(votos)
    print(f"\n--- PARTIDOS POR ENCIMA DEL PROMEDIO ---")
    print(f"Promedio general de todos los votos: {promedio_general:.2f}\n")
    
    indices_encima = Funciones.obtener_partidos_mas_votos(votos, promedio_general)
    if len(indices_encima) == 0:
        print("[!] Ningún partido supera el promedio general.")
    else:
        porcentaje_acumulado = 0
        for idx in indices_encima:
            porcentaje = (votos[idx] / total_votos) * 100
            print(f"Partido {idx + 1}: {votos[idx]} votos | Porcentaje: {porcentaje:.2f}%")
            porcentaje_acumulado += porcentaje
        print(f"\nPorcentaje acumulado de los resultados: {porcentaje_acumulado:.2f}%")

def mostrar_menos_votado(votos: list) -> None:
    """Muestra el o los partidos menos votados del sistema."""
    total_votos = Funciones.calcular_suma_votos(votos)
    indices_minimos = Funciones.obtener_partidos_menos_votados_con_empate(votos)
    print(f"\n--- PARTIDO MENOS VOTADO ---")
    for idx in indices_minimos:
        porcentaje = (votos[idx] / total_votos) * 100
        print(f"Partido {idx + 1}: {votos[idx]} votos | Porcentaje: {porcentaje:.2f}%")

def mostrar_verificacion_balotaje(votos: list) -> None:
    """Determina analíticamente si un candidato superó el 50% de los votos."""
    total_votos = Funciones.calcular_suma_votos(votos)
    print(f"\n--- VERIFICAR SEGUNDA VUELTA ---")
    necesita_balotaje = True
    ganador_idx = -1
    
    for i in range(len(votos)):
        porcentaje = (votos[i] / total_votos) * 100
        if porcentaje > 50.0:
            necesita_balotaje = False
            ganador_idx = i
            break
            
    if necesita_balotaje:
        print("Debe realizarse una segunda vuelta electoral")
    else:
        print("No debe realizarse una segunda vuelta electoral")
        porcentaje_ganador = (votos[ganador_idx] / total_votos) * 100
        print(f"Ganador -> Partido {ganador_idx + 1}: {votos[ganador_idx]} votos ({porcentaje_ganador:.2f}%)")

def mostrar_lista_nombres(lista_ordenada: list) -> None:
    """
    Imprime en pantalla una lista de nombres de partidos de manera formateada.
    Recibe: Una lista de strings (ya ordenada).
    Devuelve: Nada (solo imprime).
    """
    print("\n--- LISTA DE PARTIDOS ORDENADA ALFABÉTICAMENTE ---")
    for nombre in lista_ordenada:
        print(f"- {nombre}")