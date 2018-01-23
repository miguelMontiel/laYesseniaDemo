import codecs as loscodecs
import openpyxl
from pprint import pprint

# Este programa va a leer los archivos que se crean en Creardic_Ventanas.py y va a convertir los valores del texto generado
# en un directorio, en el cual los Stubs del mismo van a ser las llaves, y conforme se vayan encontrando Ventanas, se van
# a ir agregando a las llaves donde se repitan.

def conversionDiccionario():
    archivo = loscodecs.open("C:/Users/IBM_ADMIN/PycharmProjects/laYesseniaDemo/ExcelReal/txts/programasUsanProgramasPrincipales.txt", "r")
    workbook = openpyxl.load_workbook("excelPrueba.xlsx")
    sheet = workbook["Sheet1"]
    print(archivo)
    print(workbook, sheet)

    dicStub_Ventana = dict()

    for linea in archivo:
        lineaSplit = linea.split()
        miStub = lineaSplit[0]
        miVentana = lineaSplit[1]

        if miStub in dicStub_Ventana:
            dicStub_Ventana[miStub].append(miVentana)

        else:
            dicStub_Ventana[miStub] = [miVentana]

    for key in dicStub_Ventana.keys():
        #Imprimer el Stub junto con todas las ventanas que tiene adjuntas.
        print(key, "contiene:", dicStub_Ventana[key])

    for row in sheet.iter_cols(min_row = 1, min_col = 1, max_row = 6000, max_col = 3):
        for cell in row:
            stubExcel = str(cell.value)
            if stubExcel in dicStub_Ventana.keys():
                ventanaCell = "B" + str(cell.row)
                ventanasFinal = str(dicStub_Ventana[stubExcel]).replace("'", "").replace("[", "").replace("]", "").replace(",", "\n").replace(" ", "")
                print(ventanaCell, ":", ventanasFinal)

                sheet[ventanaCell] = ventanasFinal

    #pprint(dicStub_Ventana)
    archivo.close()
    workbook.save("excelPrueba2.xlsx")

conversionDiccionario()