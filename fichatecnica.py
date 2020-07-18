#!/usr/bin/env python
#_*_coding: utf8_*_

import os
import sys
from time import sleep
from string import Template

os.system("cls")
def main():
    #abriendo archivo
    filein = open("Template/index.html")

    #leyendo archivo
    src = Template(filein.read())

    os.system("cls")

    print("*****************************")
    print()
    print("*  Bienvenidos al Programa  *")
    print()
    print("*****************************")
    input()
    os.system("cls")

    #Dato del documento
    fname = input("Primer Nombre: ").title()
    sname = input("Segundo Nombre: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    flastname = input("Primer Apellido: ").title()
    slastname = input("Segundo Apellido: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    cid = input("Cedula de Identidad: ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    f_nac = input("Fecha de Nacimiento: ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    nac = input("Nacionalidad: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    l_nac = input("Lugar de Nacimiento: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    estcivil = input("Estado Civil: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    sexo = input("Sexo: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    telef = input("Telefono: ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    direccion = input("Dirección: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    email = input("Correo electronico: ").lower().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    estudios = input("Estudios: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    ingreso = input("Fecha de Ingreso (DD/MM/AAAA): ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    curriculum = input("Curriculum Vitae: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    titulo = input("Titulo: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    ecedu = input("Cedula Entregada: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    doc_entregados = " ".replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    fon_Isa = input("Certificado de Afiliación: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    afp = input("Certificados de AFP: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    cargo = input("Cargo: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    pay = input("Forma de Pago: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    instalacion = input("Instalacion: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    s_liquido = input("Sueldo liquido: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    print()
    print("** Recoleccion de Tallas **")
    print()
    polera = input("Talla de Poleras: ").upper()
    pantalon = input("Talla de Pantalón: ").upper()
    chal_Geo = input("Talla de Chaleco Geólogo: ").upper()
    parca = input("Talla de Parca: ").upper()
    mic_polar = input("Talla de Micro Polar: ").upper()
    overol = input("Talla de Overol: ").upper()
    zapatos = input("Talla de Zapatos: ").upper()
    pant_termico = input("Talla de Pantalón Termico: ").upper()
    cont_eme = input("Contacto de emergencia: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
    info_adic = input("Informacion adicional importante: ").capitalize().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")

    #Cambiar algun valor antes de agregar al Diccionario

    while True:
        print('\n¿Desea editar algun campo de informacion (S/N)? \n')
        cambio = input('-----> ')
        if cambio == "S" or cambio == "s":
            os.system("cls")
            print("""
    *Menu opciones: Presione el numero*
    *del campo que desea cambiar:*

    1 - Primer Nombre
    2 - Segundo Nombre
    3 - Primer Apellido
    4 - Segundo Apellido
    5 - RUT
    6 - Fecha de Nacimiento
    7 - Nacionalidad
    8 - Lugar de Nacimiento
    9 - Estado Civil
    10 - Sexo
    11 - Telefono
    12 - Direccion
    13 - Correo Electronico
    14 - Estudios
    15 - Fecha de Ingreso
    16 - Curriculum Vitae
    17 - Titulo
    18 - Cedula Entregada
    19 - Documentos Entregados
    20 - Certificado de Afiliacion
    21 - Certificados de AFP
    22 - Cargo
    23 - Forma de Pago
    24 - Instalacion
    25 - Sueldo liquido
    26 - Talla de Polera
    27 - Talla de Pantalon
    28 - Talla de Chaleco Geologo
    29 - Talla de Parca
    30 - Talla de Micro Polar
    31 - Talla de Overol
    32 - Talla de Zapatos
    33 - Talla de Pantalon Termico
    34 - Contacto de Emergencia
    35 - Informacion Adicional Importante
    \n""")

            opcmb = input("Indique el numero del campo: ")
            if opcmb == "1":
                fname = input("Primer Nombre: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "2":
                sname = input("Segundo Nombre: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "3":
                flastname = input("Primer Apellido: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "4":
                slastname = input("Segundo Apellido: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "5":
                cid = input("Cedula de Identidad: ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "6":
                f_nac = input("Fecha de Nacimiento: ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "7":
                nac = input("Nacionalidad: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "8":
                l_nac = input("Lugar de Nacimiento: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "9":
                estcivil = input("Estado Civil: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "10":
                sexo = input("Sexo: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "11":
                telef = input("Telefono: ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "12":
                direccion = input("Dirección: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "13":
                email = input("Correo electronico: ").lower().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "14":
                estudios = input("Estudios: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "15":
                ingreso = input("Fecha de Ingreso (DD/MM/AAAA): ").upper().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "16":
                curriculum = input("Curriculum Vitae: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "17":
                titulo = input("Titulo: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "18":
                ecedu = input("Cedula Entregada: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "19":
                print("\nEsta opcion nn puede modificarse.")
            elif opcmb == "20":
                fon_Isa = input("Certificado de Afiliación: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "21":
                afp = input("Certificados de AFP: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "22":
                cargo = input("Cargo: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "23":
                pay = input("Forma de Pago: ").capitalize().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "24":
                instalacion = input("Instalacion: ").capitalize().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "25":
                s_liquido = input("Sueldo liquido: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "26":
                polera = input("Talla de Poleras: ").upper()
            elif opcmb == "27":
                pantalon = input("Talla de Pantalón: ").upper()
            elif opcmb == "28":
                chal_Geo = input("Talla de Chaleco Geólogo: ").upper()
            elif opcmb == "29":
                parca = input("Talla de Parca: ").upper()
            elif opcmb == "30":
                mic_polar = input("Talla de Micro Polar: ").upper()
            elif opcmb == "31":
                overol = input("Talla de Overol: ").upper()
            elif opcmb == "32":
                zapatos = input("Talla de Zapatos: ").upper()
            elif opcmb == "33":
                pant_termico = input("Talla de Pantalón Termico: ").upper()
            elif opcmb == "34":
                cont_eme = input("Contacto de emergencia: ").title().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            elif opcmb == "35":
                info_adic = input("Informacion adicional importante: ").capitalize().replace("á","&aacute").replace("é","&eacute").replace("í","&iacute").replace("ó","&oacute").replace("ú","&uacute").replace("ü","&uacute").replace("ñ","&ntilde")
            else:
                print("\nLa opcion no es correcta.\n")


        elif cambio == "N" or cambio == "n":
            break
        else:
            print("\nLa opcion no es correcta.")

    fullname = fname + flastname

    #Diccionario de datos
    d = {'fname': fname,
        'sname': sname,
        'f_nac': f_nac,
        'flastname': flastname,
        'slastname': slastname,
        'telef': telef,
        'sexo': sexo,
        'estcivil': estcivil,
        'email': email,
        'instalacion': instalacion,
        'cid': cid,
        'pay': pay,
        'nac': nac,
        'direccion': direccion,
        's_liquido': s_liquido,
        'doc_entregados': doc_entregados,
        'curriculum': curriculum,
        'estudios': estudios,
        'titulo': titulo,
        'fon_Isa': fon_Isa,
        'ecedu': ecedu,
        'afp': afp,
        'ingreso': ingreso,
        'cargo': cargo,
        'polera': polera,
        'pantalon': pantalon,
        'chal_Geo': chal_Geo,
        'parca': parca,
        'mic_polar': mic_polar,
        'overol': overol,
        'zapatos': zapatos,
        'pant_termico': pant_termico,
        'l_nac': l_nac,
        'cont_eme': cont_eme,
        'info_adic': info_adic}

    #Sustituyendo los valores
    result = src.substitute(d)

    try:
        os.mkdir("{}".format(fullname))
        sleep(1)
        filein2 = open('{}/'.format(fullname)+str(cid)+ '.html','w')
        sleep(1)
        filein2.writelines(result)
        sleep(1)
        print("\nCreando carpeta..\n")
        sleep(1)
        print("Guardando archivos..\n")
        print()
        sleep(1)
    except OSError:
        if os.path.exists("perfiles"):
            filein2 = open('perfiles/'+str(cid)+ '.html','w')
            filein2.writelines(result)
            print("Guardando archivos..")
            filein.close()
            filein2.close()

    while True:
        print('¿Desea salir del sistema (S/N)? \n')
        pregunta = input('----->')
        if pregunta == "N" or pregunta == "n":
            os.system(r"fichatecnica.py")
        elif pregunta == "S" or pregunta == "s":
            sys.exit()


if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print("\n\nSaliendo...")
