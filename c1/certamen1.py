import json

# Abriendo un archivo JSON desde el sistema de archivos
with open('clash_royale.json', 'r') as archivo:
    datos = json.load(archivo)

# Ahora `datos` es un diccionario de Python con los datos del archivo JSON
