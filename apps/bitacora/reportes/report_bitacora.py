# -*- coding: utf-8 -*-
import class_pdf


def gen_res_bitacora(diccionario, usuario, desde, hasta):
    # Instancia de la clase heredada L es horizontal y P es vertical

    #print "DATOS: "+str(diccionario)
    #for accion in diccionario:
    #    print accion[0]+" "+accion[1]+" "+str(accion[2])

    pdf = class_pdf.PDFBitacora(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

    #pdf.set_title(title)
    pdf.set_author('José Solorzano')
    pdf.alias_nb_pages()  # LLAMADA DE PAGINACIÓN
    pdf.add_page()  # AÑADE UNA NUEVA PAGINACIÓN
    #pdf.set_font('Times','',10)  # TAMANO DE LA FUENTE
    pdf.set_font('Arial', 'B', 15)
    pdf.set_fill_color(157, 188, 201)  # COLOR DE BOLDE DE LA CELDA
    pdf.set_text_color(24, 29, 31)  # COLOR DEL TEXTO
    pdf.set_margins(15, 10, 10)  # MARGENE DEL DOCUMENTO
    #pdf.ln(20) # Saldo de linea
    # 10 y 50 eje x y y 200 dimencion
    #pdf.line(10, 40, 200, 40) Linea

    pdf.set_fill_color(255, 255, 255)
    pdf.set_font('Arial', '', 7)
    pdf.set_y(0)
    pdf.set_x(84)
    pdf.write(30, "REPÚBLICA BOLIVARIANA DE VENEZUELA".decode("UTF-8"))
    pdf.set_y(4)
    pdf.set_x(73)
    pdf.write(30, "FRENTE UNIDO DE MOTOTAXISTAS DEL ESTADO ARAGUA".decode("UTF-8"))
    pdf.set_y(8)
    pdf.set_x(97)
    pdf.write(30, "R.I.F. J-403723125".decode("UTF-8"))
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(20)

    pdf.set_font('Arial', 'B', 10)
    pdf.cell(140, 5, "".decode("UTF-8"), '', 0, 'L', 0)
    pdf.cell(50, 4, "".decode("UTF-8"), '', 0, 'L', 0)
    pdf.ln(15)
    pdf.cell(190, 4, "BITACORA DEL USUARIO: "+usuario.upper().decode("UTF-8"), '', 1, 'C', 1)
    pdf.ln(3)
    pdf.cell(190, 4, "(DESDE: "+str(desde.replace('-', '/'))+" HASTA: "+str(hasta.replace('-', '/'))+")", '', 1, 'C', 1)

    pdf.ln(5)

    # Fila de la cabezara de la tabla
    pdf.set_font('Arial', 'B', 8)
    pdf.set_fill_color(241, 92, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(10, 5, "N°".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(30, 5, "USUARIO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(110, 5, "ACCIÓN".decode("UTF-8"), 'LTBR', 0, 'C', 1)
    pdf.cell(40, 5, "FECHA".decode("UTF-8"), 'LTBR', 1, 'C', 1)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    j = 0
    item = 0
    i = 1  # Contador de páginas
    k = 1  # Contador de registros

    for accion in diccionario:
        #print accion
        # Prueba de limitación de registros a partir de la segunda página
        #limite = 40
        #
        #if i > 1:
        #    limite = 30

        if j == 40:
            pdf.add_page()
            i += 1
            pdf.set_fill_color(255, 255, 255)
            pdf.set_font('Arial', '', 7)
            pdf.set_y(0)
            pdf.set_x(84)
            pdf.write(30, "REPÚBLICA BOLIVARIANA DE VENEZUELA".decode("UTF-8"))
            pdf.set_y(4)
            pdf.set_x(73)
            pdf.write(30, "FRENTE UNIDO DE MOTOTAXISTAS DEL ESTADO ARAGUA".decode("UTF-8"))
            pdf.set_y(8)
            pdf.set_x(97)
            pdf.write(30, "R.I.F. J-403723125".decode("UTF-8"))
            pdf.set_font('Arial', 'B', 10)
            pdf.ln(20)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(140, 5, "".decode("UTF-8"), '', 0, 'L', 0)
            pdf.cell(50, 4, "Fecha Emisión: 26/05/20".decode("UTF-8"), '', 1, 'L', 1)
            pdf.ln(5)
            pdf.cell(190, 4, "BITACORA DEL USUARIO: "+usuario.upper().decode("UTF-8"), '', 1, 'C', 1)
            pdf.ln(5)

            # Fila de la cabezara de la tabla
            pdf.set_font('Arial', 'B', 8)
            pdf.set_fill_color(241, 92, 0)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(10, 5, "N°".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(30, 5, "USUARIO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(110, 5, "ACCIÓN".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(40, 5, "FECHA".decode("UTF-8"), 'LTBR', 1, 'C', 1)
            pdf.set_fill_color(255, 255, 255)
            pdf.set_text_color(0, 0, 0)
            # Fin Cabezera
            j = 0

        #format_fecha = "%s/%s/%s" % (accion.fecha.day, accion.fecha.month, accion.fecha.year)
        #format_hora = "%s:%s:%s" % (accion.fecha.hour, accion.fecha.minute, accion.fecha.second)

        pdf.set_font('Arial', '', 8)
        pdf.cell(10, 5, str(k).decode("UTF-8"), 'LTBR', 0, 'C', 1)
        pdf.cell(30, 5, accion[1].decode("UTF-8"), 'LTBR', 0, 'L', 1)
        pdf.cell(110, 5, accion[0].encode("UTF-8").decode("UTF-8"), 'LTBR', 0, 'L', 1)
        pdf.cell(40, 5, str(accion[2]), 'LTBR', 1, 'R', 1)

        j = j + 1
        k = k + 1

    nombre_archivo = 'bitacora_'+usuario+'_('+desde+'_'+hasta+').pdf'
    pdf.output('reporte/'+nombre_archivo, 'F')
    archivo = open('reporte/'+nombre_archivo, "r")
    return archivo, nombre_archivo
