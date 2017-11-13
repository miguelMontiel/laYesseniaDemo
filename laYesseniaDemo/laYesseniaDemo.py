import codecs

# Estoy abriendo el archivo y metiendolo en la variable 'archivo'
archivo = open("Archivo.txt")
archivoNuevo = codecs.open("ArchivoNuevo.txt", "w", "utf-8")

# Por cada linea en el archivo.
for linea in archivo:
    # Si es T, escribe Aplicativa, etc etc..
    if linea.strip()[-1] == "T":
        archivoNuevo.write("Aplicativa \n")
    elif linea.strip()[-1] == "G":
        archivoNuevo.write("General \n")
    elif linea.strip()[-1] == "S":
        archivoNuevo.write("Semi-Flexible \n")
    else:
        archivoNuevo.write("N/A \n")
archivo.close()