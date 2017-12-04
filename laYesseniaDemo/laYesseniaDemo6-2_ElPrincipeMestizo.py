import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

buscarStubs = 'import gnp.to.servidor.'
buscarPaneles = 'import gnp.to.componentes.'

print("Dentro de cada una de estas clases de ventana se encuentran Stubs y paneles", "\n")

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/mainUser/Desktop/to/cliente/", title = "Archivos java")
archivoNuevoFinal = open("C:/Users/mainUser/Desktop/nuevos/ventanasUsanStubs.txt", "w+")
archivoNuevoFinal2 = open("C:/Users/mainUser/Desktop/nuevos/stubsUsanVentanas.txt", "w+")

stubs = []
ventanas = []

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    #print(os.path.basename(str(individuales[:-5])))
    #archivoNuevoFinal.write(os.path.basename(str(individuales[:-5])) + "\n")

    #print(" Stubs: ")
    #archivoNuevoFinal.write("   Stubs: " + "\n")
    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarStubs in linea:
            #print("     ", lineaStrip[23:-1])
            if lineaStrip[23:-1] not in stubs:
                stubs.append(lineaStrip[23:-1])
                #archivoNuevoFinal.write("       " + lineaStrip[23:-1] + "\n")

        for stub in stubs:
            if buscarStubs in linea:
                if stub in lineaStrip[23:-1]:
                    if os.path.basename(str(individuales[:-5])) not in ventanas:
                        ventanas.append(os.path.basename(str(individuales[:-5])))
                        #   print(stub, " tiene: ", os.path.basename(str(individuales[:-5])))
    #print(ventanas)
    '''
    print(" Paneles: ")
    #archivoNuevoFinal.write("   Paneles: " + "\n")
    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarPaneles in linea:
            print("     ", lineaStrip[26:-1])
            #archivoNuevoFinal.write("       " + lineaStrip[26:-1] + "\n")
    '''

    #archivoNuevoFinal.write("\n")
    archivo.close()