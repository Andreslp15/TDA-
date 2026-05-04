def leer_archivo(ruta_archivo):
    if not ruta_archivo:
        return None

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = [linea.strip() for linea in archivo.readlines() if linea.strip() ]
    except FileNotFoundError:
        print(f"Archivo no encontrado. Por favor ingrese una ruta correcta.")
        return None
    except IOError:
        print(f"Error al leer el archivo. Por favor intente nuevamente.")
        return None

    if not lineas:
        print("No se ha encontrado ningun dato a analizar")
        return None

    try:
        dias = int(lineas[0])

        if dias <= 0:
            print("El numero de dias debe ser mayor a 0")
            return None

        if len(lineas) < (2 * dias + 1):
            print("No se proporcionaron la cantidad de datos solicitados")
            return None

        esfuerzos = [0]
        energias = [0]

        for i in range(1, dias + 1):
            esfuerzo = int(lineas[i])
            if esfuerzo < 0:
                print("Los esfuerzos no deben ser negativos")
                return None

            esfuerzos.append(esfuerzo)

        for i in range(dias + 1, 2 * dias + 1):
            energia = int(lineas[i])
            if energia < 0:
                print("Las energias no deben ser negativas")
                return None

            if len(energias) > 1 and energia > energias[-1]:
                print("Las energias deben ser de mayor a menor")
                return None

            energias.append(energia)

    except ValueError:
        print("Los datos ingresados no son validos")
        return None

    return dias, esfuerzos, energias