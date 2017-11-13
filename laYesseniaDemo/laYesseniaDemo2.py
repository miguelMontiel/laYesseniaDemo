import codecs

archivo = open("Archivo.txt")
archivoNuevo = codecs.open("ArchivoNuevo.txt", "w", "utf-8")

# Por cada linea en el archivo.
for linea in archivo:
    if linea[1:3] == "AE":
        archivoNuevo.write("Arquitectura de Ejecución \n")
    elif linea[1:3] == "AO":
        archivoNuevo.write("Arquitectura de Operación \n")
    elif linea[1:3] == "AC":
        archivoNuevo.write("Contratación Accidentes \n")
    elif linea[1:3] == "CA":
        archivoNuevo.write("Conectividad \n")
    elif linea[1:3] == "AG":
        archivoNuevo.write("Certificación de Agentes \n")
    elif linea[1:3] == "AR":
        archivoNuevo.write("Admón. de Recursos \n")
    elif linea[1:3] == "AT":
        archivoNuevo.write("Administrador de Cupones \n")
    elif linea[1:3] == "BD":
        archivoNuevo.write("Admón. Base Datos \n")
    elif linea[1:3] == "BK":
        archivoNuevo.write("Backups \n")
    elif linea[1:3] == "CC":
        archivoNuevo.write("Call Center \n")
    elif linea[1:3] == "CD":
        archivoNuevo.write("Canales de distribución \n")
    elif linea[1:3] == "CE":
        archivoNuevo.write("Contratación \n")
    elif linea[1:3] == "CF":
        archivoNuevo.write("Contratación Flotas \n")
    elif linea[1:3] == "CG":
        archivoNuevo.write("Coaseguro \n")
    elif linea[1:3] == "CI":
        archivoNuevo.write("Contratación Fase I \n")
    elif linea[1:3] == "CS":
        archivoNuevo.write("Siniestros Cesvi Vin \n")
    elif linea[1:3] == "CV":
        archivoNuevo.write("Contratación Vida \n")
    elif linea[1:3] == "DI":
        archivoNuevo.write("Conector Distribuidores \n")
    elif linea[1:3] == "DW":
        archivoNuevo.write("Data Warehouse \n")
    elif linea[1:3] == "FI":
        archivoNuevo.write("Fiscal \n")
    elif linea[1:3] == "MA":
        archivoNuevo.write("Migración de Datos Autos \n")
    elif linea[1:3] == "MC":
        archivoNuevo.write("Componentes Comunes \n")
    elif linea[1:3] == "MD":
        archivoNuevo.write("Migración de Datos Daños \n")
    elif linea[1:3] == "MG":
        archivoNuevo.write("Migración de Datos Gastos Médicos \n")
    elif linea[1:3] == "MK":
        archivoNuevo.write("Marketing \n")
    elif linea[1:3] == "MV":
        archivoNuevo.write("Migración de Datos Vida \n")
    elif linea[1:3] == "OP":
        archivoNuevo.write("Operadores Centro de Computo \n")
    elif linea[1:3] == "PE":
        archivoNuevo.write("Personas \n")
    elif linea[1:3] == "PC":
        archivoNuevo.write("archivoNuevo.write Center \n")
    elif linea[1:3] == "PR":
        archivoNuevo.write("Planeación y Control de la producción \n")
    elif linea[1:3] == "RB":
        archivoNuevo.write("Recibos \n")
    elif linea[1:3] == "RE":
        archivoNuevo.write("Reaseguro \n")
    elif linea[1:3] == "SC":
        archivoNuevo.write("Sistema de Cabinas \n")
    elif linea[1:3] == "SG":
        archivoNuevo.write("Saga \n")
    elif linea[1:3] == "SI":
        archivoNuevo.write("Siniestros \n")
    elif linea[1:3] == "SM":
        archivoNuevo.write("Sistema de Mediadores \n")
    elif linea[1:3] == "SP":
        archivoNuevo.write("Soporte a la Producción \n")
    elif linea[1:3] == "ST":
        archivoNuevo.write("Soporte Técnico \n")
    elif linea[1:3] == "SS":
        archivoNuevo.write("Servicios de Salud \n")
    elif linea[1:3] == "SV":
        archivoNuevo.write("Siniestros Vida \n")
    elif linea[1:3] == "TC":
        archivoNuevo.write("Tablas Corporativas \n")
    elif linea[1:3] == "TM":
        archivoNuevo.write("Aplicaciones Temporales \n")
    elif linea[1:3] == "TO":
        archivoNuevo.write("Tesorería Operativa \n")
    elif linea[1:3] == "VG":
        archivoNuevo.write("Replicación de tablas Vignette \n")
    elif linea[1:3] == "TP":
        archivoNuevo.write("Taller de Productos \n")
    else:
        archivoNuevo.write("N/A \n")

archivo.close()