import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

busqueda = input("Que se va a buscareishon: ")

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/", title = "Archivos java")
archivoNuevo = open("programasUsanProgramasPrincipales.txt", "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    nombreArchivo = os.path.basename(str(individuales[:-5]))
    print(nombreArchivo, ": ")
    archivoNuevo.write(nombreArchivo + ": ")

    for linea in archivo:
        if busqueda in linea:
            print(linea)
            archivoNuevo.write(linea)

    archivoNuevo.write("\n")
    print("")
    archivo.close()

archivoNuevo.close()