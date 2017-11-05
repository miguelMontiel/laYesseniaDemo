# Estoy abriendo el archivo y metiendolo en la variable 'archivo'
archivo = open("Archivo.txt")

# Por cada linea en el archivo.
for linea in archivo:
    if linea.strip()[-1] == "T":
        print("Aplicativa")
    elif linea.strip()[-1] == "G":
        print("General")
    elif linea.strip()[-1] == "S":
        print("Semi-Flexible")
    else:
        print("N/A")
archivo.close()