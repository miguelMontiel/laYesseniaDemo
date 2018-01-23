import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

buscarStubs = 'import gnp.to.servidor.'

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/PycharmProjects/laYesseniaDemo/ExcelReal/INFOPRE/cliente/", title = "Archivos java")
archivoNuevo = "C:/Users/IBM_ADMIN/PycharmProjects/laYesseniaDemo/ExcelReal/txts/StubsconProgramas.txt"
archivoNuevoFinal = open(archivoNuevo, "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    nombreArchivo = os.path.basename(str(individuales[:-5]))

    for linea in archivo:
        lineaStrip = linea.strip()
        if buscarStubs in linea:
            miStub = lineaStrip[23:-1]
            if '//' not in lineaStrip[:2] and miStub[:5] != 'Ktoli' and miStub[:5] != 'Ktolv':
                print("Stub: ", miStub)
                archivoNuevoFinal.write(miStub)
                print(" Ventana: ",  nombreArchivo)
                archivoNuevoFinal.write(" " + nombreArchivo + "\n")
                print("")
    archivo.close()
archivoNuevoFinal.close()