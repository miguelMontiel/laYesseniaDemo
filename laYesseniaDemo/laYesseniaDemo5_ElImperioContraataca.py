import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

'''Stubs'''

buscarProgramas = 'setNoServicioCics(obtenerNombreServicio("'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/INFOPRE/PreINFO-27Abril2016/src/gnp/to/servidor/", title = "Archivos java")
archivoNuevo = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/stubsUsanProgramas.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

print("Por cada Stub que hay aqui, se tienen los programas que se muestras abajo del mismo.", "\n")
archivoNuevoFinal.write("Por cada Stub que hay aqui, se tienen los programas que se muestras abajo del mismo." + "\n")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    nombreArchivo = os.path.basename(str(individuales[:-5]))

    if nombreArchivo[:4] != 'Ktol':
        #archivoNuevoFinal.write("Stub: " + nombreArchivo + "\n")
        print(nombreArchivo)
        for linea in archivo:
            if buscarProgramas in linea:
                lineaStrip = linea.strip()
                print(lineaStrip[41:49])
                archivoNuevoFinal.write("Programa: " + lineaStrip[41:49] + "\n")
                archivoNuevoFinal.write("Stub: " + nombreArchivo + "\n")
        print("")
        archivoNuevoFinal.write("\n")
    archivo.close()