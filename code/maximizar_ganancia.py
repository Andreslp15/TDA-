from leer_archivo import leer_archivo

def maximizar_esfuerzo(dias, esfuerzos, energias):

    ganancia = [[0] * (dias + 2) for i in range(dias + 2)]

    for dia in range(dias, 0, -1):
        for posicion in range(1, dia + 1):
            ganancia_minima_entrenando = min(esfuerzos[dia], energias[posicion])
            valor_entrenando = (ganancia_minima_entrenando + ganancia[dia + 1][posicion + 1])
            valor_descanso = ganancia[dia + 1][1]

            ganancia[dia][posicion] = max(valor_entrenando, valor_descanso)

    ganancia_optima = ganancia[1][1]

    return ganancia_optima, ganancia

def reconstruir_solucion(ganancias, dias, esfuerzos, energias):

    entrenamientos = []

    dia = 1
    posicion = 1

    while dia <= dias:

        ganancia_minima_entrenando = min(esfuerzos[dia], energias[posicion])
        valor_entrenamiento = ganancia_minima_entrenando + ganancias[dia + 1][posicion + 1]

        if ganancias[dia][posicion] == valor_entrenamiento:
            entrenamientos.append("Entrenar")
            posicion += 1
        else:
            entrenamientos.append("Descansar")
            posicion = 1

        dia += 1

    return entrenamientos
