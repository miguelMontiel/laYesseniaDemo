import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

'''Ventanas'''

buscarStubs = 'import gnp.to.servidor.'
buscarPaneles = 'import gnp.to.componentes.'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/mainUser/Desktop/to/cliente/", title = "Archivos java")
archivoNuevo = "C:/Users/mainUser/Desktop/nuevos/ventanasUsanStubs.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales[:-5])))
    archivoNuevoFinal.write(os.path.basename(str(individuales)) + "\n")

    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarStubs in linea:
            miStub = lineaStrip[23:-1]
            if '//' not in lineaStrip[:2]:
                print(" Stub: ", miStub)
                archivoNuevoFinal.write("   Stub:" + miStub + "\n")

        if buscarPaneles in linea:
            miPanel = lineaStrip[26:-1]
            if '//' not in lineaStrip[:2]:
                print(" Panel: ", miPanel)
                archivoNuevoFinal.write("   Panel:" + miPanel + "\n")

    archivoNuevoFinal.write("\n")
    print("")
    archivo.close()