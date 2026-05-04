# TP2 Programación Dinámica

En este proyecto desarrollamos un plan de entrenamiento óptimo para el problema que
presenta Scaloni al momento de planificar los entrenamientos de la Selección Argentina
para salir campeona en la próxima Copa del Mundo.

## Índice

* [Descripción del Problema](#descripción-del-problema)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Requisitos](#requisitos)
* [Ejecución del Algoritmo](#ejecución-del-algoritmo)
* [Pruebas Manuales](#pruebas-manuales)
* [Formato de Archivos de Entrada](#formato-de-archivos-de-entrada)
* [Mediciones de Complejidad](#mediciones-de-complejidad)

## Descripción del Problema

Scaloni debe definir un plan de entrenamientos en los $n$ días próximos al mundial.
Cada día tiene un esfuerzo $e_i$. La energía de los jugadores disminuye a medida que
entrenan días consecutivos ($s_1, s_2, \dots, s_n$). Si deciden descansar, la energía se
resetea a $s_1$ al día siguiente.

Nuestro objetivo es implementar un algoritmo mediante programación dinámica que nos defina
el plan de entrenamiento para que de esa manera podamos obtener en los $n$ días la mayor
ganancia posible y poder tener más probabilidad de poder quedarnos con la Copa del Mundo.

## Estructura del Proyecto

```bash
tp2/
├── code/
│   ├── tp2.py
│   ├── maximizar_ganancia.py
│   ├── ganancia_backtracking.py 
│   └── mediciones.py      
├── ejemplos/
│   ├── 3.txt 
│   ├── 10_bis.txt
│   ├── 1000.txt
│   ├── ejemplo2.txt
│   └── vacio.txt
├── img/
│   ├── complejidad.png
├── .gitignore                     
├── Informe                     
├── Makefile              
├── README.md
└── requerimientos.txt
```
## Requisitos

1. Python 3x...
2. numpy
3. matplotlib
4. scipy
5. seaborn

## Ejecución del Algoritmo

La ejecución del programa se realiza desde la raíz del proyecto. Puedes hacerlo de
las siguientes formas:

*Opcion 1:* Ejecución directa
```bash
python3 code/tp2.py ejemplos/3.txt
```
*Opción 2:* Otorgando permisos de ejecución

```bash
chmod +x code/tp2.py
./code/tp2.py ejemplos/3.txt
```

*Opción 3:* Utilizando el Makefile

```bash
make run FILE=ejemplos/3.txt
```

**Aclaración sobre `make`:** Si no cuentas con Makefile instalado, puedes instalar
el make ejecutando el siguiente comando:

```bah
sudo apt update && sudo apt install make
```

En las distribuciones basadas en Debian, como Ubuntu. En caso de tener MacOs lo puedes
instalar ejecutando:

```bash
brew install make
```

## Formato de archivos de entrada

Para que el programa funcione correctamente, los archivos de entrada deben cumplir
con la siguiente estructura, conteniendo únicamente con valores numéricos:

```txt
3      <--- Cantidad de días (n)
90     <---
100    <--- Esfuerzos requeridos por cada día (n valores)
50     <---
100    <---
50     <--- Energía disponible por cada día consecutivo (n valores)
15     <---
```

## Pruebas manuales

Para corroborar el correcto funcionamiento y la optimalidad del algoritmo, puedes ejecutar las pruebas provistas.
Desde la raíz del proyecto podemos ejecutar:

```bash
python3 code/tp2.py ejemplos/3.txt
```

Salida esperada:

```txt
La ganancia optima es: 7
El plan de entrenamiento es:
Dia 1: Descansar
Dia 2: Entrenar
Dia 3: Entrenar
```

## Mediciones de complejidad

Para generar los gráficos de complejidad y análisis empírico,
el proyecto utiliza un entorno virtual para aislar las dependencias gráficas. Proveemos un
archivo `Makefile` que automatiza todo este proceso.

*Utilizando Makefile*

```bash
make mediciones
```

Si solo quieres instalar el entorno virtual sin ejecutar las mediciones lo puedes realizar
ejecutando:

```bash
make install
```

*Forma manual:*

Si prefieres realizar el proceso manualmente sin ejecutar `make`, ejecuta la siguiente
secuencia de comandos:

```bash
# 1. Crear y activar el entorno virtual
python3 -m venv venv 
source venv/bin/activate

# 2. Instalar requerimientos
pip install -r requerimientos.txt

# 3. Ejecutar el script de mediciones
python3 code/mediciones.py
```









