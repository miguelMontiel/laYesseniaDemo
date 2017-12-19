import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

archivos = Tkinter.askopenfilenames(initialdir = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/", title = "Archivos java")
archivoNuevo = open("programasUsanProgramasPrincipales.txt", "w+")

for individuales in archivos:
    archivo = loscodecs.open(individuales, "r")
    nombreArchivo = os.path.basename(str(individuales[:-5]))

    print("------------------------- " + nombreArchivo + " -------------------------")
    archivoNuevo.write("------------------------- " + nombreArchivo + " -------------------------" + "\n")

    for linea in archivo:
        if ".to.cliente" in linea and "package" not in linea:
            print(linea)
            archivoNuevo.write(linea)

        if "ventana" in linea and "= new" in linea:
            if ".ae." not in linea:
                print(linea)
                archivoNuevo.write(linea)

    archivoNuevo.write("\n" + "\n")
    print("")
    archivo.close()

archivoNuevo.close()