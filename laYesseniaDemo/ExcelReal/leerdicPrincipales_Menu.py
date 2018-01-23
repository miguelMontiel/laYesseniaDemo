import openpyxl
from pprint import pprint

def conversionDiccionario():
    archivo = open("C:/Users/IBM_ADMIN/PycharmProjects/laYesseniaDemo/ExcelReal/txts/menuUsanProgramasPrincipales.txt", "r", encoding = 'utf-8')

    dicVentana_Menu = dict()

    for linea in archivo:
        lineaSplit = linea.split("-")
        miMenu = lineaSplit[0]
        miVentanaPrincipal = lineaSplit[1].replace("\n", "")

        if miMenu in dicVentana_Menu:
            dicVentana_Menu[miVentanaPrincipal].append(miMenu)

        else:
            dicVentana_Menu[miVentanaPrincipal] = [miMenu]

    archivo.close()
    leerExcel(dicVentana_Menu)

def leerExcel(dicVentana_Menu):
    workbook = openpyxl.load_workbook("excelPrueba2.xlsx")
    sheet = workbook["Sheet1"]

    dicPrincipal_menu = dict()

    for row in sheet.iter_cols(min_row = 1, min_col = 1, max_row = 6000, max_col = 3):
        for cell in row:
            stubExcel = str(cell.value).split("\n")
            for valorStubExcel in stubExcel:
                if valorStubExcel in dicVentana_Menu.keys():
                    ventanaCell = "C" + str(cell.row)
                    menusFinal = str(dicVentana_Menu[valorStubExcel]).replace("'", "").replace("[", "").replace("]", "").replace(",", "\n")

                    if ventanaCell in dicPrincipal_menu:
                            dicPrincipal_menu[ventanaCell].append(menusFinal)

                    else:
                        dicPrincipal_menu[ventanaCell] = [menusFinal]

    for keys in dicPrincipal_menu.keys():
        sheet[keys] = str(dicPrincipal_menu[keys]).replace("'", "").replace("[", "").replace("]", "").replace(",", "\n")

    workbook.save("excelPrueba3.xlsx")

conversionDiccionario()