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

hneader_center = ParagraphStyle(
    "header_center",
    fontSize=9,       # Un poco más grande que las celdas normales
    leading=11,
    alignment=TA_CENTER,
    textColor=colors.black
)
# =====================================================================================
# DATOS DE LA TABLA - ENCABEZADOS  
# =====================================================================================
# Encabezado principal dividido en dos grupos: URGENCIA Y ELECTIVA
encabezado = [
    Paragraph("<b>URGENCIA</b>", hneader_center), 
    Paragraph("<b>ELECTIVA</b>", hneader_center)
]


# FILA DE DATOS (11 FILAS)
datos_brutos = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [5,2],
    [0,0],
    [5,2],
    [0,0],
    [0,0],
    [0,0],
]

# convertimos los datos en Paragraphs para evitar problemas de formato
filas_datos = [
    [Paragraph(str(celda), cell_center) for celda in fila]
    for fila in datos_brutos
]









# =====================================================================================
#FUNCION PARA CREAR LA TABLA
# =====================================================================================
def crear_tabla_cesarea():

    pdf = SimpleDocTemplate("pdf/tabla_cesarea.pdf", pagesize=letter)

    story = []

    # titulo de la seccion

    story.append(Paragraph("<b>CESAREA</b>", styles["Title"]))

    story.append(Spacer(1, 12))


    #====================================================================================
    # CREACIÓN DE LA TABLA
    #====================================================================================

    tabla =  [encabezado] + filas_datos

    #definir ancho de columnas
    colWidths=[80, 80 ]
    

    #crear tabla con sus columnas
    t = Table(tabla, colWidths=colWidths)


    #====================================================================================
    # ESTILO DE LA TABLA
    #====================================================================================

    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.orange),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ("GRID", (0,0), (-1,-1), 1, colors.black),   
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BACKGROUND", (0,4), (-1,4), colors.red),
    ]))

    story.append(t)

    # Generar el PDF
    pdf.build(story)

    print("PDF de la tabla de cesáreas generado exitosamente.")


#=====================================================================================
# LLAMADA A LA FUNCIÓN PRINCIPAL
#=====================================================================================

if __name__ == "__main__":
    crear_tabla_cesarea()






