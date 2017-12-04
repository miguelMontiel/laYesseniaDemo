import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

buscarVentana = 'import gnp.to.cliente.'
buscarStubs = 'import gnp.to.servidor.'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/mainUser/Desktop/to/componentes/", title = "Archivos java")
archivoNuevo = "C:/Users/mainUser/Desktop/nuevos/panelesUsanVentanas.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

print("Por cada Panel que hay aqui se imprimen sus stubs y sus ventanas respectivamente.", "\n")
archivoNuevoFinal.write("Por cada Panel que hay aqui se imprimen sus stubs y sus ventanas respectivamente." + "\n")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    print(os.path.basename(str(individuales[:-5])))
    archivoNuevoFinal.write(os.path.basename(str(individuales[:-5])) + "\n")

    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarVentana in linea:
            print(" Ventana: ", lineaStrip[22:-1])
            archivoNuevoFinal.write("   Ventana: " + lineaStrip[22:-1] + "\n")

        if buscarStubs in linea:
            print(" Stub: ", lineaStrip[23:-1])
            archivoNuevoFinal.write("   Stub: " + lineaStrip[23:-1] + "\n")

    archivoNuevoFinal.write("\n")
    archivo.close()
    print("")