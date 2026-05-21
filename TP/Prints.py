# Prints.py

def mostrar_menu():
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

def mostrar_error_no_cargado():
    print("\n[!] Error: Debe cargar los votos (Opción 1 u 11) antes de realizar consultas.")

def mostrar_mensaje_vacio_filtro(mensaje_error):
    print(f"\n[!] {mensaje_error}")