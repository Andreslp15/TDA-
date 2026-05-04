import time
import random
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import seaborn as sns
from ganancia_backtracking import  ganancia
from maximizar_ganancia import maximizar_esfuerzo

sns.set_theme(style="whitegrid")
random.seed(50)
np.random.seed(50)

def generador(dias):
    esfuerzos = [0] + [random.randint(1, 100) for i in range(dias)]
    energias = [0] + sorted([random.randint(1, 100) for i in range(dias)], reverse=True)
    return esfuerzos, energias

def generador_fijo_esfuerzos(dias):
    esfuerzos = [0] + [100 for i in range(dias)]
    energias = [0] + sorted([random.randint(0, 100) for i in range(dias)], reverse=True)
    return esfuerzos, energias

def generador_energia_nula(dias):
    esfuerzos = [0] + [random.randint(0, 100) for i in range(dias)]
    energias = [0] + [0 for i in range(dias)]
    return  esfuerzos, energias

def tiempos(tabla, generador, tamanios, repeticiones=3):
    promedio_tiempos = []

    for n in tamanios:
        tiempo = 0
        for veces in range(repeticiones):
            esfuerzos, energias = generador(n)
            inicio = time.perf_counter()
            tabla((int(n)), esfuerzos, energias)
            tiempo += time.perf_counter() - inicio
        promedio_tiempos.append(tiempo / repeticiones)

    return np.array(promedio_tiempos)

def complejidad_cuadratica(dias, constante1, constante2):

    return constante1 * (dias ** 2) + constante2

def complejidad_exponencial(dias, constante1, constante2):

    return constante1 * (2 ** dias) + constante2

def reporte():
    pequenios = np.arange(1, 19)
    tiempo_bt = tiempos(ganancia, generador, pequenios, repeticiones=4)

    parametros_bt, ajuste = opt.curve_fit(complejidad_exponencial, pequenios, tiempo_bt)

    grandes = np.linspace(10, 1000, 30).astype(int)
    tiempos_pd = tiempos(maximizar_esfuerzo, generador, grandes)
    tiempos_pd_fija = tiempos(maximizar_esfuerzo, generador_fijo_esfuerzos, grandes)

    parametros_pd, ajuste_pd = opt.curve_fit(complejidad_cuadratica, grandes, tiempos_pd)

    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    axs[0].scatter(pequenios, tiempo_bt, color='red', label="Mediciones BT", s=40, edgecolor='black', zorder=3)
    axs[0].plot(pequenios, complejidad_exponencial(pequenios, *parametros_bt), 'r--', label="Ajuste teorico $O(2^n)$")
    axs[0].set_title("Exponencial Backtracking", fontsize=16, fontweight='bold')
    axs[0].set_xlabel("Dias", fontsize=14)
    axs[0].set_ylabel("Tiempo (s)", fontsize=14)
    axs[0].legend()

    axs[1].scatter(grandes, tiempos_pd, color='blue', label="Mediciones aleatorias PD", alpha=0.6, s=30)
    axs[1].scatter(grandes, tiempos_pd_fija, color='purple', label="Mediciones esfuerzo fijo PD", alpha=0.5, s=30)

    axs[1].plot(grandes, complejidad_cuadratica(grandes, *parametros_pd), color='navy', linestyle='--', linewidth=2, label="Ajuste teorico $O(n²)$.")
    axs[1].set_title("Complejidad Cuadratica", fontsize=16, fontweight='bold')
    axs[1].set_xlabel("Dias", fontsize=14)
    axs[1].set_ylabel("Tiempo (s)", fontsize=14)
    axs[1].legend()

    plt.tight_layout()
    plt.savefig("img/complejidad.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    reporte()


