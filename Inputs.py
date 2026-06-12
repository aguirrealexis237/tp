# Inputs.py

def es_cadena_numerica(cadena):
    if len(cadena) == 0:
        return False
    for i in range(len(cadena)):
        caracter = cadena[i]
        if ord(caracter) < 48 or ord(caracter) > 57:
            return False
    return True

def pedir_votos_partido(mensaje):
    while True:
        entrada = input(mensaje)
        if es_cadena_numerica(entrada):
            numero = int(entrada)
            if numero > 0:
                return numero  # <-- AQUÍ: Debe retornar el número y salir de la función
            else:
                print("Error: La cantidad de votos debe ser mayor a cero.")
        else:
            print("Error: Entrada inválida. Ingrese un número entero.")