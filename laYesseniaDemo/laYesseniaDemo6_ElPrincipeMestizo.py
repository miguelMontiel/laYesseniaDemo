import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

inicio = 'import gnp.to.servidor.'
archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/INFOPRE/PreINFO-27Abril2016/src/gnp/to/servidor/", title = "Archivos java")
archivoNuevo = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/archivoNuevo2.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales)))
    archivoNuevoFinal.write(os.path.basename(str(individuales)) + "\n")
    for linea in archivo:
        if inicio in linea:
            lineaStrip = linea.strip()
            if lineaStrip[31:32] == ";":
                print(lineaStrip[23:31])
                archivoNuevoFinal.write("   " + lineaStrip[23:31] + "\n")

    archivoNuevoFinal.write("\n" + "\n")
    archivo.close()
    print("\n")