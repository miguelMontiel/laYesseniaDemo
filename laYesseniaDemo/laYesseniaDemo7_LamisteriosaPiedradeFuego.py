import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

'''Paneles'''

buscarVentana = 'import gnp.to.cliente.'
buscarStubs = 'import gnp.to.servidor.'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/INFOPRE/PreINFO-27Abril2016/src/gnp/to/componentes/", title = "Archivos java")
archivoNuevo = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/panelesUsanVentanas.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales[:-5])))
    #archivoNuevoFinal.write(os.path.basename(str(individuales[:-5])) + "\n")

    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarVentana in linea:
            print(" Ventana: ", lineaStrip[22:-1])
            #archivoNuevoFinal.write("   " + lineaStrip[22:-1] + "\n")

        if buscarStubs in linea:
            print(" Stub: ", lineaStrip[23:-1])

    #archivoNuevoFinal.write("\n" + "\n")
    archivo.close()
    print("\n")