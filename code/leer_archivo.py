def leer_archivo(ruta_archivo):
    if not ruta_archivo:
        return None

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print(f"Archivo no encontrado. Por favor ingrese una ruta correcta.")
        return None
    except IOError:
        print(f"Error al leer el archivo. Por favor intente nuevamente.")
        return None

    if not lineas:
        print("No se ha encontrado ningun dato a analizar")
        return None

    dias = 0
    esfuerzos = [0]
    energias = [0]

    if lineas[0].startswith("S"):
        lineas = lineas[1:]

    for linea in lineas:
        try:
            dia, esfuerzo, energia = map(int, linea.strip().split(','))
            esfuerzos.append(esfuerzo)
            energias.append(energia)
            dias += 1
        except ValueError:
            print(f"La linea {linea.strip()} no tiene el formato correcto.")
            return None

    return dias, esfuerzos, energias