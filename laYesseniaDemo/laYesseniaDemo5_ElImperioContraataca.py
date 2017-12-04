import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

buscarProgramas = 'setNoServicioCics(obtenerNombreServicio("'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/mainUser/Desktop/to/servidor/", title = "Archivos java")
archivoNuevo = "C:/Users/mainUser/Desktop/nuevos/stubsUsanProgramas.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

print("Por cada Stub que hay aqui, se tienen los programas que se muestras abajo del mismo.", "\n")
archivoNuevoFinal.write("Por cada Stub que hay aqui, se tienen los programas que se muestras abajo del mismo." + "\n")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales[:-5])))
    archivoNuevoFinal.write(os.path.basename(str(individuales[:-5])) + "\n")

    for linea in archivo:
        if buscarProgramas in linea:
            lineaStrip = linea.strip()
            print(lineaStrip[41:49])
            archivoNuevoFinal.write("   " + lineaStrip[41:49] + "\n")

    print("")
    archivoNuevoFinal.write("\n")
    archivo.close()