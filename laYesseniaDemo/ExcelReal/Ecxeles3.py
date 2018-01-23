import openpyxl
import tkinter.filedialog as Tkinter
import os.path
import codecs as loscodecs

prueba = {
    'prueba1':'1prueba',
    'prueba2':'2prueba',
    'prueba3':'3prueba',
    'prueba4':'4prueba'}

print(prueba.values())

def InsertarEntradaSalida():
    workbook = openpyxl.load_workbook("excelPrueba.xlsx")
    sheet = workbook["Sheet1"]

    for row in sheet.iter_cols(min_row = 1, min_col = 1, max_row = 2, max_col = 2):
        for cell in row:
            entradaSalida = str(cell.value)
            print(entradaSalida)
            prueba2 = str(prueba.values())
            prueba3 = prueba2.replace("'", "")
            prueba3 = prueba3.replace(",", "\n")
            prueba3 = prueba3.replace("(", "")
            prueba3 = prueba3.replace("[", "")
            prueba3 = prueba3.replace(")", "")
            prueba3 = prueba3.replace("]", "")
            prueba3 = prueba3.replace("dict_values", "")
            print(prueba3)
            sheet['B1'] = prueba3
            '''
            if entradaSalida in dicEntradaSalida.keys():
                entrada = "H" + str(cell.row)
                salida = "I" + str(cell.row)

                for valores in dicEntradaSalida[entradaSalida]:
                    celdaEntrada = sheet[entrada]
                    sheet[salida] = valores


                #for valores in dicEntradaSalida[cell.value]:
                    #print(valores)

                    if valores[:5] == 'Ktoli':
                        Ktoli = valores[:5]
                        entrada = "H" + str(cell.row)
                        print(entrada, dicEntradaSalida)
                            #if valores2.startswith(Ktoli):
                                #print(entrada, ": ", dicEntradaSalida[Ktoli])
                       #sheet[entrada] = entradaSalidaValores
                    elif valores[:5] == 'ktolv':
                        ktolv = valores[:5]
                        salida = "I" + str(cell.row)
                        print(entradaSalidaValores[ktolv])
                        #sheet[salida] = entradaSalidaValores
                    '''

    workbook.save("excelPrueba2.xlsx")

InsertarEntradaSalida()