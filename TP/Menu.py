# Menu.py (VERSIÓN DE DIAGNÓSTICO DIRECTO)
import Inputs
import Prints
import Funciones

def ejecutar_menu():
    votos_partidos = []
    
    while True:
        Prints.mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "0":
            print("\nSaliendo...")
            break

        elif opcion == "1":
            votos_partidos = [] 
            print("\n--- CARGA SECUENCIAL DE VOTOS (5 Partidos) ---")
            for i in range(5):
                partido_votos = Inputs.pedir_votos_partido(f"Ingrese votos para el Partido {i + 1}: ")
                votos_partidos.append(partido_votos)
            
            print("\n[✓] Llegamos al final de la Opción 1 sin rompernos.")
            print(f"Datos en memoria: {votos_partidos}")
            input("Presione ENTER para regresar al menú...")

        elif opcion == "11":
            votos_partidos = [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]
            print("\n[✓] Vector hardcodeado cargado.")
            input("Presione ENTER para regresar al menú...")

        elif opcion == "2":
            print(f"\n--- INTENTANDO MOSTRAR VOTOS ---")
            print(f"Vector actual: {votos_partidos}")
            # Si se rompe acá, el problema es la función calcular_suma_votos en Funciones.py
            total_votos = Funciones.calcular_suma_votos(votos_partidos)
            print(f"Total de votos calculados de forma manual: {total_votos}")
            
            cant_partidos = len(votos_partidos)
            for i in range(cant_partidos):
                porcentaje = (votos_partidos[i] / total_votos) * 100
                print(f"Partido {i + 1}: {votos_partidos[i]} votos | Porcentaje: {porcentaje:.2f}%")
            input("\nPresione ENTER para regresar al menú...")
            
        else:
            print("\nOpción no configurada en este test o inválida.")
            input("Presione ENTER para continuar...")