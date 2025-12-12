# =====================================================================================
# IMPORTACIONES NECESARIAS PARA GENERAR EL PDF
# =====================================================================================
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

# Cargamos estilos por defecto como Title, Normal, etc.
styles = getSampleStyleSheet()

# =====================================================================================
# DEFINICIÓN DE ESTILOS PERSONALIZADOS PARA CELDAS Y ENCABEZADOS
# =====================================================================================

# Estilo para celdas con números (centrados)
cell_center = ParagraphStyle(
    "cell_center",
    fontSize=8,      # Tamaño similar a Excel
    leading=10,      # Altura de línea
    alignment=TA_CENTER
)

# Estilo para encabezados (centrados y más grandes)
header_center = ParagraphStyle(
    "header_center",
    fontSize=9,       # Un poco más grande que las celdas normales
    leading=11,
    alignment=TA_CENTER,
    textColor=colors.black
)


# =====================================================================================
# DATOS DE LA TABLA - ENCABEZADOS
# =====================================================================================

# Encabezado principal dividido en dos grupos: EUTÓCICO y DISTÓCICO
encabezado_superior = [
    Paragraph("<b>EUTÓCICO</b>", header_center), "", "",
    Paragraph("<b>DISTÓCICO</b>", header_center), "", ""
]

# Encabezado inferior (subcolumnas)
encabezado_inferior = [
    Paragraph("<b>&lt;28 semanas</b>", header_center),
    Paragraph("<b>28 a 37 semanas</b>", header_center),
    Paragraph("<b>38 semanas y más</b>", header_center),
    Paragraph("<b>&lt;28 semanas</b>", header_center),
    Paragraph("<b>29 a 37 semanas</b>", header_center),
    Paragraph("<b>39 semanas y más</b>", header_center),
]


# =====================================================================================
# FILAS DE DATOS (13 FILAS)
# =====================================================================================

datos_brutos = [
    [1,19,35,0,1,1],
    [0,0,0,0,0,0],
    [0,4,15,0,0,1],
    [1,19,48,0,1,2],
    [1,19,45,0,1,1],
    [0,16,40,0,1,2],
    [0,10,29,0,0,1],
    [0,9,28,0,0,2],
    [1,19,35,0,1,1],
    [0,"","",0,"",""],   # fila con celdas vacías
    [0,0,0,0,0,0],
    [0,19,45,0,0,2],
    [0,22,46,0,0,2],
]

# Convertimos todos los valores a Paragraph para evitar problemas de formato
filas_datos = [
    [Paragraph(str(x), cell_center) for x in fila]
    for fila in datos_brutos
]












# =====================================================================================
# FUNCIÓN PRINCIPAL PARA GENERAR EL PDF
# =====================================================================================

def generar_pdf_eutocico_distocico():

    # Creamos el PDF en carpeta /pdf
    pdf = SimpleDocTemplate("pdf/tabla_eutocico_distocico.pdf", pagesize=letter)

    story = []

    # ----- TÍTULO DE LA SECCIÓN -----
    story.append(
        Paragraph("<b>EUTÓCICO vs DISTÓCICO</b> <b>''REM 21''</b>", styles["Title"])
    )
    story.append(Spacer(1, 10))  # Espacio debajo del título


    # =================================================================================
    # CONSTRUCCIÓN COMPLETA DE LA TABLA
    # =================================================================================

    tabla = [
        encabezado_superior,
        encabezado_inferior,
    ] + filas_datos   # Agrega las 13 filas de datos


    # Definir ancho de columnas (6 columnas)
    col_widths = [90, 90, 90, 90, 90, 90]


    # Crear tabla con sus columnas
    t = Table(tabla, colWidths=col_widths)



    # =================================================================================
    # APLICAR ESTILOS DE TABLA
    # =================================================================================

    t.setStyle(TableStyle([

        # ----- COLOR DE FONDO PARA ENCABEZADO SUPERIOR (EUTÓCICO / DISTÓCICO) -----
        ("BACKGROUND", (0,0), (2,0), colors.lightgrey),       # EUTÓCICO
        ("BACKGROUND", (3,0), (5,0), colors.lightgrey),       # DISTÓCICO

        # ----- COLOR DE FONDO PARA EL ENCABEZADO INFERIOR -----
        ("BACKGROUND", (0,1), (-1,1), colors.khaki),

        # ----- GRID GENERAL -----
        ("GRID", (0,0), (-1,-1), 1, colors.black),

        # ----- ALINEACIÓN VERTICAL -----
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),

        # ----- FUSIÓN DE CELDAS EN ENCABEZADO SUPERIOR -----
        ("SPAN", (0,0), (2,0)),  # EUTÓCICO
        ("SPAN", (3,0), (5,0)),  # DISTÓCICO

        # ----- FILA ROJA (MISMA QUE EN EXCEL) -----
        ("BACKGROUND", (0,9), (-1,9), colors.red),
    ]))


    # Agregamos tabla al PDF
    story.append(t)

    # Guardamos el PDF
    pdf.build(story)

    print("PDF de la tabla generado correctamente ")



# =====================================================================================
# EJECUCIÓN DIRECTA DEL SCRIPT
# =====================================================================================
if __name__ == "__main__":
    generar_pdf_eutocico_distocico()
