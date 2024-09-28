import os
import re


def cabecera():
    # Cabecera
    print("                                                                                                   ")
    print("  ▓█████▄ ▓█████   ██████   ▄████  ██▓     ▒█████    ██████   ██████ ▓█████  ██▀███    For Intouch ")
    print("  ▒██▀ ██▌▓█   ▀ ▒██    ▒  ██▒ ▀█▒▓██▒    ▒██▒  ██▒▒██    ▒ ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒  exported:   ")
    print("  ░██   █▌▒███   ░ ▓██▄   ▒██░▄▄▄░▒██░    ▒██░  ██▒░ ▓██▄   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒  DB.CSV      ")
    print("  ░▓█▄   ▌▒▓█  ▄   ▒   ██▒░▓█  ██▓▒██░    ▒██   ██░  ▒   ██▒  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄                ")
    print("  ░▒████▓ ░▒████▒▒██████▒▒░▒▓███▀▒░██████▒░ ████▓▒░▒██████▒▒▒██████▒▒░▒████▒░██▓ ▒██▒  By 3xpl01tz ")
    print("   ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░ ░▒   ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░  v_0.0.16    ")
    print("   ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░  ░   ░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░              ")
    print("   ░ ░  ░    ░   ░  ░  ░  ░ ░   ░   ░ ░   ░ ░ ░ ▒  ░  ░  ░  ░  ░  ░     ░     ░░   ░               ")
    print("     ░       ░  ░      ░        ░     ░  ░    ░ ░        ░        ░     ░  ░   ░                   ")
    print("   ░                                                                                               ")
    print()

def error():
    limpiar_pantalla()

    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢉⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠄⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣉⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣈⡏⠹⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣦⡀⠀⠈⣿⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠃⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠘⣿⣤⡀⢀⡀⠀⠀⠉⠻⡟⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢉⣁⣡⣤⣴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣹⣿⣾⢿⣆⣠⠀⠀⢁⠈⣿⡿⠀⠈⣿⠟⠀⠈⠹⣿⡏⠀⠀⠈⣿⡟⠁⠸⣿⠃⣼⣏⢀⡆⣴⣿⣿⡟⡅⣿⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣹⣿⡿⢿⣶⣷⣼⣷⣟⠁⠀⠀⡟⠀⠀⠀⠀⣽⡇⠀⠀⠀⠨⠄⠀⠀⢙⡀⢃⣸⣾⣿⣼⣿⢸⣧⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣷⡈⣷⡈⣻⣿⣼⣦⣀⣰⠃⠀⠀⠀⠀⠙⠁⠀⡀⠀⠊⣠⣀⣤⣾⣷⡌⣯⣿⢟⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡺⠇⢹⣿⣿⣿⡿⣿⣤⣀⣀⣤⣤⣴⣄⠀⠃⣄⣀⢿⡿⠛⠿⣿⠙⣿⣷⣼⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⠹⣿⡿⠁⢹⡃⠈⠉⣿⠁⠊⡿⠀⠈⣿⠀⢸⡇⠀⠀⢿⡄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⠁⣠⣾⠇⠀⢠⣧⠀⢠⡇⠀⢀⣿⡀⢸⣇⠀⢠⣸⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣦⣠⣾⣿⣶⣾⣷⣤⣸⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")

def ayuda():
    limpiar_pantalla()

    print("[#] Explicacion de los modos:\n")

    print("\t[+] 1. Desglosar CSV")
    print("\t\t Separara los grupos en distintos archivos el DB.CSV generado por el InTouch [IOAccess, IOInt...]")
    print("\t\t Nota: Estos archivos son 100% compatibles con el DBLoad de InTouch")
    print()
    print("\t[+] 2. Desglosar CSV a formato legible en Excel")
    print("\t\t Desglosa el DB.CSV en archivos legibles para el Excel. Al abrirlos sera necesario usar como ")
    print("\t\t delimitador \"|\" y el Calificador de texto: Ninguno")
    print("\t\t Nota: Estos archivos no son importables al InTouch, para ello es necesario usar el modo 3")
    print()
    print("\t[+] 3. Convertir Carpeta Excel a Intouch")
    print("\t\t Convierte los archivos generados en el modo 2 para importarlo al InTouch")
    print("\t\t Nota: Estos archivos son 100% compatibles con el DBLoad de InTouch")

def menu():
    # Menu
    print("[#] Seleccione un modo:\n")
    print("\t[+] 1. Desglosar CSV")
    print("\t[+] 2. Desglosar CSV a formato legible en Excel")
    print("\t[+] 3. Convertir Carpeta Excel a Intouch")
    print()
    print("\t[+] 99. Ayuda")

    seleccion_modo = input("\n[!] Seleccione un modo: ")
    print()

    if seleccion_modo == "1":
        listar_archivos(0)
        nombre_archivo = input("[!] Introduce el nombre del archivo a desglosar: ")
        desglosar_CSV(nombre_archivo)
        esperar_tecla()
    elif seleccion_modo == "2":
        listar_archivos(0)
        nombre_archivo = input("[!] Introduce el nombre del archivo a desglosar: ")
        desglosar_CSV_a_Excel(nombre_archivo)
        esperar_tecla()
    elif seleccion_modo == "3":
        listar_archivos(1)
        nombre_carpeta = input("[!] Introduce el nombre de la carpeta a combertir: ").replace("\\", "")
        convertir_Excel_a_InTouch(nombre_carpeta)
        esperar_tecla()
    elif seleccion_modo == "99":
        ayuda()
        esperar_tecla()
        limpiar_pantalla()
        menu()
    else:
        error()
        esperar_tecla()

def listar_archivos(type):
    # Tipos de archivo
    #   0. Archvivo
    #   1. Carpeta


    limpiar_pantalla()

    # Obtiene la lista de archivos y carpetas en el directorio actual
    elementos = os.listdir()

    # Imprime la lista de archivos y carpetas
    if type == 0:
        print("[#] Archivos locales:\n")
    elif type == 1:
        print("[#] Carpetas locales:\n")


    for elemento in elementos:
        ruta = os.path.join(os.getcwd(), elemento)

        if os.path.isfile(ruta) and type == 0:
            print("\t[+] " + elemento)
        elif os.path.isdir(ruta) and type == 1:
            print("\t[+] \\" + elemento + "\\")
    print()

def desglosar_CSV(nombre_archivo):
    limpiar_pantalla()

    print("[#] Desglosando el archvio:\t.\\" + nombre_archivo)

    # Creacion de la carpeta de los archivos de salida
    directorio_salida = nombre_archivo + "_Desglose"
    os.makedirs(directorio_salida, exist_ok=True)
    print("[+] Carpeta Creada: \t\t.\\" + directorio_salida + "\\")

    archivo_salida = None  # Inicializar la variable fuera del bucle

    # Apertura del Archivo CSV
    with open(nombre_archivo, 'r', encoding='latin-1') as archivo_lectura:

        # Recorro la primera columna linea a linea en busca de los grupos
        for linea in archivo_lectura:
            columnas = linea.split(',')
            primera_columna = columnas[0].strip()

            # Si encontramos un grupo y no es ":mode=*" lo memorizamos como archivo de salida
            if re.search(r"^:", primera_columna) and not re.match(r'^:mode=', primera_columna):
                archivo_salida = "DB_" + primera_columna.replace(':', '') + ".CSV"

                # Verificar si el archivo ya existe y eliminarlo si es así
                ruta_archivo = os.path.join(directorio_salida, archivo_salida)
                if os.path.exists(ruta_archivo):
                    os.remove(ruta_archivo)
                    print("[!] Archivo Antiguo Eliminado: \t.\\" + ruta_archivo)

                # Mostrar en pantalla el nuevo archivo a crear
                print("[+] Archivo Creado: \t\t.\\" + directorio_salida + "\\" + archivo_salida)


            # Si se ha encontrado un grupo se guardan las líneas dentro de ese grupo
            if archivo_salida:

                linea_leida = None

                # Verificar si el archivo no existe y en ese caso le añadimos ":mode=replace"
                ruta_archivo = os.path.join(directorio_salida, archivo_salida)
                if not os.path.exists(ruta_archivo):
                    linea_leida = (":mode=replace\n" + linea)
                else:
                    linea_leida = linea

                # Creacion del Archivo
                with open(os.path.join(directorio_salida, archivo_salida), "a", encoding='latin-1', newline="") as archivo_escritura:
                    archivo_escritura.write(linea_leida)

def desglosar_CSV_a_Excel (nombre_archivo):
    limpiar_pantalla()

    print("[#] Desglosando el archvio:\t.\\" + nombre_archivo)

    # Creacion de la carpeta de los archivos de salida
    directorio_salida = nombre_archivo + "_Desglose_Excel"
    os.makedirs(directorio_salida, exist_ok=True)
    print("[+] Carpeta Creada: \t\t.\\" + directorio_salida + "\\")

    archivo_salida = None  # Inicializar la variable fuera del bucle

    # Apertura del Archivo CSV
    with open(nombre_archivo, 'r', encoding='latin-1') as archivo_lectura:

        # Recorro la primera columna linea a linea en busca de los grupos
        for linea in archivo_lectura:
            columnas = linea.split(',')
            primera_columna = columnas[0].strip()

            # Si encontramos un grupo y no es ":mode=*" lo memorizamos como archivo de salida
            if re.search(r"^:", primera_columna) and not re.match(r'^:mode=', primera_columna):
                archivo_salida = "DB_" + primera_columna.replace(':', '') + ".CSV"

                # Verificar si el archivo ya existe y eliminarlo si es así
                ruta_archivo = os.path.join(directorio_salida, archivo_salida)
                if os.path.exists(ruta_archivo):
                    os.remove(ruta_archivo)
                    print("[!] Archivo Antiguo Eliminado: \t.\\" + ruta_archivo)

                # Mostrar en pantalla el nuevo archivo a crear
                print("[+] Archivo Creado: \t\t.\\" + directorio_salida + "\\" + archivo_salida)

            # Si se ha encontrado un grupo se guardan las líneas dentro de ese grupo
            if archivo_salida:

                linea_leida = None

                # Verificar si el archivo no existe y en ese caso le añadimos ":mode=replace"
                ruta_archivo = os.path.join(directorio_salida, archivo_salida)
                if not os.path.exists(ruta_archivo):
                    linea_leida = (":mode=replace\n" + procesar_linea_a_csv_excel(linea))
                else:
                    linea_leida = procesar_linea_a_csv_excel(linea)

                # Creacion del Archivo
                with open(os.path.join(directorio_salida, archivo_salida), "a", encoding='latin-1',
                          newline="") as archivo_escritura:
                    archivo_escritura.write(linea_leida)

def convertir_Excel_a_InTouch(carpeta_origen):
    limpiar_pantalla()

    # Carpeta de destino
    carpeta_destino = carpeta_origen.replace("_Excel", "") + "_InTouch"

    print("[#] Convirtiendo archivos de \t.\\" + carpeta_origen + "\\* a .\\" + carpeta_destino + "\\*")

    # Crear la carpeta de destino si no existe
    os.makedirs(carpeta_destino, exist_ok=True)
    print("[+] Carpeta creada: \t\t.\\" + carpeta_destino + "\\")

    # Obtener la lista de archivos en la carpeta de origen
    archivos = os.listdir(carpeta_origen)

    # Procesar y copiar archivos línea por línea
    for archivo in archivos:
        ruta_origen = os.path.join(carpeta_origen, archivo)
        if os.path.isfile(ruta_origen):
            ruta_destino = os.path.join(carpeta_destino, archivo)
            with open(ruta_origen, 'r', encoding='latin-1') as archivo_lectura, \
                 open(ruta_destino, 'w', encoding='latin-1', newline='') as archivo_escritura:

                for linea in archivo_lectura:
                    # Procesar cada línea según tus necesidades
                    # Por ejemplo, eliminar comillas duplicadas y escribir la línea en el nuevo archivo
                    nueva_linea = procesar_linea_a_csv_Intouch(linea)


                    #nueva_linea = agregar_comillas_a_prim_col(nueva_linea)

                    archivo_escritura.write(nueva_linea)

            print("[+] Archivo convertido: \t.\\" + carpeta_destino + "\\" + archivo)

def procesar_linea_a_csv_excel(linea):
    # Reemplazar comas dentro de comillas por un carácter especial, por ejemplo, #
    linea_temp = re.sub(r'"(.*?)"', lambda x: x.group(0).replace(',', '#'), linea)

    # Reemplazar todas las comas por punto y coma
    linea_temp = linea_temp.replace(',', '|')

    # Reemplazar el carácter especial # por comas
    linea_modificada = linea_temp.replace('#', ',')

    return linea_modificada

def procesar_linea_a_csv_Intouch(linea):

    linea_temp = linea

    # Si es la primera linea del archivo elimino los delimitadores que ha añadido el Excel
    if linea.startswith(':mode='):
        linea_temp = linea_temp.replace(';', '')
        linea_temp = linea_temp.replace(',', '')

    # Reemplazar todas las comas por punto y coma
    linea_temp = linea_temp.replace('|', ';')       # Por si no se ha abierto el archivo en el excel
    linea_temp = linea_temp.replace(';', ',')       # Por si se ha ha abierto el archivo en el excel

    # Reemplazar Triples Comillas Generadas por el Excel
    linea_temp = linea_temp.replace('"""', '"')

    # Añadir Comillas a la Primera Columna Siempre que no sea la Cabecera
    if not linea.startswith(':'):
        partes = linea_temp.split(',')

        # Verificar si hay al menos una parte después del split
        if partes:
            # Verificar si la primera palabra no tiene comillas, luego agregarlas
            if not partes[0].startswith('"') and not partes[0].endswith('"'):
                partes[0] = f'"{partes[0]}"'

        # Unir las partes modificadas de nuevo en un string
        linea_temp = ','.join(partes)

    linea_modificada = linea_temp

    return linea_modificada

def agregar_comillas_a_prim_col(linea):
    partes = linea.split(',')

    # Verificar si hay al menos una parte después del split
    if partes:
        # Verificar si la primera palabra no tiene comillas, luego agregarlas
        if not partes[0].startswith('"') and not partes[0].endswith('"'):
            partes[0] = f'"{partes[0]}"'

    # Unir las partes modificadas de nuevo en un string
    nueva_linea = ','.join(partes)

    return nueva_linea

def limpiar_pantalla():

    sistema_operativo = os.name

    if sistema_operativo == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

    cabecera()

def cambiar_color():

    if os.name == 'nt':  # Windows
        import ctypes

        # Constantes para los colores de la consola en Windows
        FOREGROUND_BLACK = 0x0000
        FOREGROUND_BLUE = 0x0001
        FOREGROUND_GREEN = 0x0002
        FOREGROUND_RED = 0x0004
        FOREGROUND_INTENSITY = 0x0008
        BACKGROUND_BLUE = 0x0010
        BACKGROUND_GREEN = 0x0020
        BACKGROUND_RED = 0x0040
        BACKGROUND_INTENSITY = 0x0080
        BACKGROUND_YELLOW = 0x0060

        # Funciones de la API de Windows
        STD_OUTPUT_HANDLE = -11
        GetStdHandle = ctypes.windll.kernel32.GetStdHandle
        SetConsoleTextAttribute = ctypes.windll.kernel32.SetConsoleTextAttribute

        # Obtener el identificador de la consola
        handle = GetStdHandle(STD_OUTPUT_HANDLE)

        # Cambiar el color de fondo de la consola a azul
        SetConsoleTextAttribute(handle, FOREGROUND_INTENSITY | FOREGROUND_GREEN | FOREGROUND_INTENSITY)

        # Restaurar el color de fondo a su valor predeterminado (negro)
        # SetConsoleTextAttribute(handle, 0x07)

    else:  # Linux
        # Utilizar secuencias de escape ANSI para cambiar el color de fondo a amarillo
        print("\033[43m")

def esperar_tecla():
    input("\nPresiona enter para salir... ")



if __name__ == "__main__":
    # Cambiar el directorio de trabajo al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    cambiar_color()
    cabecera()
    menu()


