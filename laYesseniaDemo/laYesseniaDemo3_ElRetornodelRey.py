with open('Archivo.txt', 'r') as archivo:
    with open('Archivo2.txt', 'r') as archivo2:
        same = set(archivo).intersection(archivo2)

same.discard('\n')

with open('ArchivoNuevo.txt', 'w') as archivoNuevo:
    for linea in same:
        archivoNuevo.write(linea)

archivo.close()
archivo2.close()