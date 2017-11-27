import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

'''Ventanas'''

buscarStubs = 'import gnp.to.servidor.'
buscarPaneles = 'import gnp.to.componentes.'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/INFOPRE/PreINFO-27Abril2016/src/gnp/to/cliente/", title = "Archivos java")
archivoNuevo = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/ventanasUsanStubs.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales[:-5])), " contiene: ")
    #archivoNuevoFinal.write(os.path.basename(str(individuales)) + "\n")

    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarStubs in linea:
            print(" Stub: ", lineaStrip[23:-1])
            #archivoNuevoFinal.write("   " + lineaStrip[23:-1] + "\n")

        if buscarPaneles in linea:
            print(" Panel: ", lineaStrip[26:-1])
            #archivoNuevoFinal.write("   " + lineaStrip[26:-1] + "\n")

    #archivoNuevoFinal.write("\n" + "\n")
    print("")
    archivo.close()