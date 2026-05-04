#!/usr/bin/env python3
import sys
from leer_archivo import leer_archivo
from maximizar_ganancia import maximizar_esfuerzo, reconstruir_solucion

def main():

    if len(sys.argv) != 2:
        print("No se han proporcionado los parametros suficientes")
        return

    ruta_archivo = sys.argv[1]
    datos = leer_archivo(ruta_archivo)

    if datos is not None:

        dias, esfuerzos, energias = datos

        ganancia_optima, tabla = maximizar_esfuerzo(dias, esfuerzos, energias)
        camino = reconstruir_solucion(tabla, dias, esfuerzos, energias)

        if ganancia_optima is None:
            print("Los datos pasados son invalidos")
            return

        print(f"La ganancia optima es: {ganancia_optima}")
        print("El plan de entrenamiento es: ")

        for dia, accion in enumerate(camino, 1):
            print(f"Dia {dia}: {accion}")

if __name__ == "__main__":
    main()