# -*- coding: utf-8 -*-
import class_pdf

import os

from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia


def gen_res_linea(agremiados, fecha, datos_linea):
    # Instancia de la clase heredada L es horizontal y P es vertical
    print datos_linea
    cod_linea = ""
    linea = ""
    presidente = ""
    telefono = ""
    estado = ""
    municipio = ""
    parroquia = ""
    direccion = ""
    for d2 in datos_linea:
        cod_linea = d2.cod_linea
        #print cod_linea
        linea = d2.linea
        #print linea
        presidente = d2.presidente
        #print presidente
        telefono = d2.telefono
        #print telefono
        estado = d2.estado.cod_estado
        #print estado
        municipio = d2.municipio
        #print municipio
        parroquia = d2.parroquia
        #print parroquia
        direccion = d2.direccion
        #print direccion

    # Obtención del nombre del estado, el municipio y la parroquia
    for e in Estado.objects.filter(cod_estado=estado):
        print e.estado
        desc_estado = e.estado
    for m in Municipio.objects.filter(estado_id=estado, cod_municipio=municipio):
        print m.municipio
        desc_municipio = m.municipio
    for p in Parroquia.objects.filter(estado_id=estado, municipio=municipio, cod_parroquia=parroquia):
        print p.parroquia
        desc_parroquia = p.parroquia

    # Captura el directorio desde la raiz del proyecto
    os.path.dirname(os.path.abspath(__file__))
    DIR_URL = os.getcwd()

    pdf = class_pdf.PDFLinea(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

    # Número de página.
    #print 'Pagina '+str(pdf.page_no())+"/"+str(pdf.alias_nb_pages())

    pdf.set_author('José Solorzano')
    pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
    pdf.add_page()  # AÑADE UNA NUEVA PAGINACION
    pdf.set_font('Arial', '', 9)
    pdf.set_fill_color(157, 188, 201)  # COLOR DE BOLDE DE LA CELDA
    pdf.set_text_color(24, 29, 31)  # COLOR DEL TEXTO
    pdf.set_margins(15, 10, 10)  # MARGENE DEL DOCUMENTO

    pdf.set_y(0)
    pdf.set_x(75)
    pdf.write(30, "REPÚBLICA BOLIVARIANA DE VENEZUELA".decode("UTF-8"))
    pdf.set_y(5)
    pdf.set_x(63)
    pdf.write(30, "FRENTE UNIDO DE MOTOTAXISTAS DEL ESTADO ARAGUA".decode("UTF-8"))
    pdf.set_y(10)
    pdf.set_x(90)
    pdf.write(30, "R.I.F. J-403723125".decode("UTF-8"))

    pdf.set_fill_color(255, 255, 255)
    pdf.set_font('Arial', '', 7)

    pdf.set_font('Arial', 'B', 10)
    pdf.ln(25)

    pdf.set_font('Arial', 'B', 10)
    pdf.cell(140, 5, "".decode("UTF-8"), '', 0, 'L', 0)
    pdf.cell(50, 4, "".decode("UTF-8"), '', 0, 'L', 0)
    pdf.ln(10)
    ########################################################################
    pdf.set_fill_color(255, 255, 255)
    pdf.set_font('Arial', 'B', 14)
    pdf.set_fill_color(240, 92, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(180, 5, "DATOS DE LA LÍNEA".decode("UTF-8"), 'LTBR', 1, 'C', 1)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(24, 29, 31)

    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "CÓDIGO".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, cod_linea.upper(), 'LTBR', 1, 'L', 1)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "NOMBRE".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, linea.upper(), 'LTBR', 1, 'L', 1)
    #pdf.set_x(51)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "PRESIDENTE".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, presidente.upper(), 'LTBR', 1, 'L', 1)
    #pdf.set_x(51)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "TELÉFONO".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, telefono.upper(), 'LTBR', 1, 'L', 1)
    #pdf.set_x(51)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "ESTADO".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, str(desc_estado).upper().decode("UTF-8"), 'LTBR', 1, 'L', 1)
    #pdf.set_x(51)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "MUNICIPIO".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, str(desc_municipio).upper().decode("UTF-8"), 'LTBR', 1, 'L', 1)
    #pdf.set_x(51)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "PARROQUIA".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, desc_parroquia.upper().encode("UTF-8").decode("UTF-8"), 'LTBR', 1, 'L', 1)
    #pdf.set_x(51)
    pdf.set_font('Arial', 'B', 9)
    pdf.cell(40, 5, "DIRECCIÓN".decode("UTF-8"), 'LTB', 0, 'L', 1)
    pdf.set_font('Arial', '', 9)
    pdf.cell(140, 5, direccion.upper(), 'LTBR', 1, 'L', 1)
    ########################################################################
    pdf.ln(8)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(180, 4, "AGREMIADOS ASOCIADOS".decode("UTF-8"), '', 1, 'C', 1)
    pdf.ln(5)

    # Fila de la cabezara de la tabla
    pdf.set_font('Arial', 'B', 9)
    pdf.set_fill_color(240, 92, 0)
    pdf.set_text_color(255, 255, 255)
    #pdf.cell(25, 5, "FOTO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(30, 5, "CÉDULA".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(91, 5, "NOMBRE COMPLETO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(20, 5, "EDAD".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(40, 5, "TELÉFONO".decode("UTF-8"), 'LTBR', 1, 'C', 1)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    i = 1  # Contador para el número de páginas
    j = 0  # Contador para los registros
    #y = 0  # Contador para el eje 'y' de las imágenes
    for agremiado in agremiados:
        #print agremiado.nacionalidad+" "+str(agremiado.cedula)+" "+str(agremiado.p_nombre).decode("UTF-8")
        cedula = agremiado.nacionalidad+"-"+str(agremiado.cedula)
        nombre = agremiado.p_nombre+" "+agremiado.s_nombre+" "+agremiado.p_apellido+" "+agremiado.s_apellido
        #f_nac = str(agremiado.fecha_nac).split("-")
        #f_nac = f_nac[2]+"-"+f_nac[1]+"-"+f_nac[0]
        edad = agremiado.edad
        tel = agremiado.tlf_movil
        tel = str(tel[0:4])+"-"+str(tel[3:])

        # y = 25

        # Limitación de registros para la primera página
        limite = 14
        # Nueva limitación de registros a partir de la segunda página
        if i > 1:
            limite = 18

        # Condicional para validar si viene la foto vacia
        if agremiado.foto == "":
            FOTO = "usuario.jpg"
        else:
            FOTO = agremiado.foto

        if j == limite:
            pdf.add_page()  # AÑADE UNA NUEVA PAGINACION
            i += 1  # Aumenta en uno el numero de páginas
            pdf.set_font('Arial', '', 9)
            pdf.set_fill_color(157, 188, 201)  # COLOR DE BOLDE DE LA CELDA
            pdf.set_text_color(24, 29, 31)  # COLOR DEL TEXTO
            pdf.set_margins(15, 10, 10)  # MARGENE DEL DOCUMENTO

            pdf.set_y(0)
            pdf.set_x(75)
            pdf.write(30, "REPÚBLICA BOLIVARIANA DE VENEZUELA".decode("UTF-8"))
            pdf.set_y(5)
            pdf.set_x(63)
            pdf.write(30, "FRENTE UNIDO DE MOTOTAXISTAS DEL ESTADO ARAGUA".decode("UTF-8"))
            pdf.set_y(10)
            pdf.set_x(90)
            pdf.write(30, "R.I.F. J-403723125".decode("UTF-8"))

            pdf.set_fill_color(255, 255, 255)
            pdf.set_font('Arial', '', 7)

            pdf.set_font('Arial', 'B', 10)
            pdf.ln(25)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(140, 5, "".decode("UTF-8"), '', 0, 'L', 0)
            pdf.cell(50, 4, "".decode("UTF-8"), '', 0, 'L', 0)
            pdf.ln(10)
            ########################################################################
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(180, 4, "AGREMIADOS ASOCIADOS".decode("UTF-8"), '', 1, 'C', 1)
            pdf.ln(5)

            # Fila de la cabezara de la tabla
            pdf.set_font('Arial', 'B', 8)
            pdf.set_fill_color(240, 92, 0)
            pdf.set_text_color(255, 255, 255)
            #pdf.cell(25, 5, "FOTO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(30, 5, "CÉDULA".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(91, 5, "NOMBRE COMPLETO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(20, 5, "EDAD".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(40, 5, "TELÉFONO".decode("UTF-8"), 'LTBR', 1, 'C', 1)
            pdf.set_fill_color(255, 255, 255)
            pdf.set_text_color(0, 0, 0)

            j = 0
            #y = 0

        pdf.set_font('Arial', '', 9)
        # Se refleja la foto del agremiado
        #print DIR_URL
        #print FOTO
        #print DIR_URL+"/foto/"+str(FOTO)
        #pdf.image(DIR_URL+"/foto/"+str(FOTO), 18, 112+y, 20)
        #pdf.cell(25, 25, "", 'LTBR', 0, 'C', 0)
        pdf.cell(30, 10, cedula, 'LTBR', 0, 'C', 1)
        pdf.cell(91, 10, nombre.encode("UTF-8").decode("UTF-8"), 'LTBR', 0, 'C', 1)
        pdf.cell(20, 10, str(edad)+" AÑOS".decode("UTF-8"), 'LTBR', 0, 'C', 1)
        pdf.cell(40, 10, tel, 'LTBR', 1, 'C', 1)

        j = j + 1
        #y = y + 25

    print "Páginas: "+str(i)

    nombre_archivo = linea+'.pdf'
    pdf.output('reporte/'+nombre_archivo, 'F')
    archivo = open('reporte/'+nombre_archivo, "r")
    return archivo, nombre_archivo
