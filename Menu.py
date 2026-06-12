# Menu.py
import Prints
import Funciones

def ejecutar_menu() -> None:
    votos_partidos = []
    
    while True:
        Prints.mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "0":
            print("\nSaliendo del sistema...")
            break

        elif opcion == "1":
            print("\n--- CARGA SECUENCIAL DE VOTOS (5 Partidos) ---")
            votos_partidos = Funciones.realizar_carga_secuencial(5)
            print("\n[✓] Votos cargados con éxito.")
            input("Presione ENTER para regresar al menú...")

        elif opcion == "11":
            votos_partidos = [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]
            print("\n[✓] Vector hardcodeado cargado correctamente (10 partidos).")
            input("Presione ENTER para regresar al menú...")

        # Validación de estado obligatoria para proteger el programa contra vectores vacíos
        elif opcion in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            if len(votos_partidos) == 0:
                Prints.mostrar_error_no_cargado()
                input("Presione ENTER para continuar...")
                continue

            if opcion == "2":
                Prints.mostrar_votos_generales(votos_partidos)
            elif opcion == "3":
                Prints.mostrar_filtro_porcentajes(votos_partidos, 10.0)
            elif opcion == "4":
                Prints.mostrar_filtro_porcentajes(votos_partidos, 15.0)
            elif opcion == "5":
                Prints.mostrar_filtro_porcentajes(votos_partidos, 20.0)
            elif opcion == "6":
                Prints.mostrar_filtro_votos_minimos(votos_partidos, 500)
            elif opcion == "7":
                Prints.mostrar_filtro_votos_minimos(votos_partidos, 1000)
            elif opcion == "8":
                Prints.mostrar_por_encima_promedio(votos_partidos)
            elif opcion == "9":
                Prints.mostrar_menos_votado(votos_partidos)
            elif opcion == "10":
                Prints.mostrar_verificacion_balotaje(votos_partidos)
                
            input("\nPresione ENTER para regresar...")

        elif opcion == "12":
            lista_nombres = ["Frente UTN", "Alianza Scarafilo", "La libertad de Baus", "Unidad de Python", "Frente de Java"]
            nombres_ordenados = Funciones.ordenar_nombres_alfabeticamente(lista_nombres)
            Prints.mostrar_lista_nombres(nombres_ordenados)
            input("\nPresione ENTER para regresar al menú...")

        else:
            print("\nOpción inválida. Intente de nuevo.")
            input("Presione ENTER para continuar...")