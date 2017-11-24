import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

inicio = 'import gnp.to.cliente.'
archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/INFOPRE/PreINFO-27Abril2016/src/gnp/to/servidor/", title = "Archivos java")
archivoNuevo = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/archivoNuevo3.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales)))
    archivoNuevoFinal.write(os.path.basename(str(individuales)) + "\n")
    for linea in archivo:
        if inicio in linea:
            lineaStrip = linea.strip()
            print(lineaStrip[22:])
            archivoNuevoFinal.write("   " + lineaStrip[22:] + "\n")

    archivoNuevoFinal.write("\n" + "\n")
    archivo.close()
    print("\n")