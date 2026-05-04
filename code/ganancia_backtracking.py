def ganancia_backtracking(dias, esfuerzos, energias, dia, posicion, ganancia, camino):

    if dia > dias:
        return ganancia, camino.copy()

    ganancia_entrenando = min(esfuerzos[dia], energias[posicion])
    camino.append("Entrenar")
    ganancia_max, camino_entrenando = ganancia_backtracking(dias, esfuerzos, energias, dia + 1, posicion + 1, ganancia + ganancia_entrenando, camino)
    camino.pop()

    camino.append("Descansar")
    ganancia_descansando, camino_descanso = ganancia_backtracking(dias, esfuerzos, energias, dia + 1,1, ganancia, camino)
    camino.pop()

    if ganancia_max > ganancia_descansando:
        return ganancia_max, camino_entrenando
    else:
        return ganancia_descansando, camino_descanso

def ganancia(dias, esfuerzos, energias):

    if dias is None or esfuerzos is None or energias is None:
        return None

    return ganancia_backtracking(dias, esfuerzos, energias, 1, 1, 0, [])

