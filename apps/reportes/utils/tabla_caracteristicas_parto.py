# ====================================================================================
# IMPORTACIONES NECESARIAS PARA GENERAR LA TABLA EN PDF
# ====================================================================================

# SimpleDocTemplate = crea el PDF completo, controla página, márgenes y contenido.
# Table = construye tablas.
# TableStyle = permite aplicar colores, borde, alineación, spans, etc.
# Paragraph = permite texto con formato HTML (negritas, saltos <br/>).
# Spacer = agrega espacios verticales entre elementos del PDF.
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# ParagraphStyle = define estilos tipográficos (tamaño, alineación, sangría, color).
# getSampleStyleSheet = carga estilos por defecto como Title, Heading1, Normal.
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# letter = establece tamaño de página tipo carta (8.5x11 pulgadas).
from reportlab.lib.pagesizes import letter

# TA_CENTER, TA_LEFT = constantes para alinear texto en celdas.
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# colors = paleta de colores HTML y predefinidos para aplicar estilos en la tabla.
from reportlab.lib import colors



# ====================================================================================
# ESTILOS PERSONALIZADOS PARA LA TABLA
# ====================================================================================

# Cargamos estilos estándar (Title, Normal...)
styles = getSampleStyleSheet()

# Estilo de texto alineado a la izquierda.
# Usado en la primera columna con texto descriptivo (ej: TOTAL PARTOS).
cell_left = ParagraphStyle(
    "cell_left",      # nombre interno
    fontSize=8,       # tamaño pequeño tipo Excel
    leading=10,       # espacio entre líneas
    alignment=TA_LEFT # alineación izquierda
)

# Estilo de texto centrado.
# Usado en la segunda columna con números.
cell_center = ParagraphStyle(
    "cell_center",
    fontSize=8,
    leading=10,
    alignment=TA_CENTER
)

# Estilo para los encabezados de la tabla.
# Son más grandes porque son títulos de categoría.
header_center = ParagraphStyle(
    "header_center",
    fontSize=10,       # tamaño mayor para encabezado
    leading=12,        # separación entre líneas adecuada
    alignment=TA_CENTER,
    textColor=colors.black
)



# ====================================================================================
# FUNCIÓN PRINCIPAL PARA GENERAR EL PDF
# ====================================================================================

def generar_pdf_caracteristicas_parto():

    # Creamos el PDF con tamaño carta.
    pdf = SimpleDocTemplate("pdf/tabla_caracteristicas_parto.pdf", pagesize=letter)

    story = []  # contenedor donde se agregan elementos (títulos, tablas, espaciadores)



    # ============================================================================
    # TÍTULO PRINCIPAL DE LA SECCIÓN
    # ============================================================================

    # Creamos título HTML con negritas
    story.append(
        Paragraph(
            "<b>CARACTERISTICAS DEL PARTO</b> <b>''REM 24''</b>",
            styles["Title"]   # usamos el estilo “Title” que viene predefinido
        )
    )

    # Espacio entre el título y la tabla (10 puntos)
    story.append(Spacer(1, 10))



    # ============================================================================
    # ENCABEZADOS DE LA TABLA (FILA SUPERIOR)
    # =================================================================================

    # Primera celda del encabezado: texto corto
    encabezado_1 = Paragraph("<b>CARACTERISTICAS DEL PARTO</b>", header_center)

    # Segunda celda del encabezado: texto largo dividido con <br/>
    # <br/> solo funciona dentro de Paragraph
    encabezado_2 = Paragraph(
        "Lactancia materna en los primeros<br/>"
        "60 minutos de vida (RN con peso<br/>"
        "de 2.500 grs. o más)",
        header_center
    )



    # =================================================================================
    # CONTENIDO DE LA TABLA PRINCIPAL
    # =================================================================================

    tabla = [
        # Primera fila = encabezados
        [encabezado_1, encabezado_2],

        # Filas con datos numéricos
        [Paragraph("TOTAL PARTOS",     cell_left), Paragraph("122", cell_center)],
        [Paragraph("VAGINAL",          cell_left), Paragraph("65",  cell_center)],
        [Paragraph("INSTRUMENTAL",     cell_left), Paragraph("0",   cell_center)],
        [Paragraph("CESÁREA ELECTIVA", cell_left), Paragraph("26",  cell_center)],
        [Paragraph("CESÁREA URGENCIA", cell_left), Paragraph("31",  cell_center)],
    ]



    # =================================================================================
    # ANCHO DE LAS COLUMNAS
    # =================================================================================
    # 300 px = primera columna (texto largo)
    # 200 px = segunda columna (números)
    col_widths = [300, 200]



    # =================================================================================
    # CREAMOS OBJETO TABLE PARA REPORTLAB
    # =================================================================================

    t = Table(tabla, colWidths=col_widths)



    # =================================================================================
    # APLICAMOS ESTILOS VISUALES A LA TABLA
    # =================================================================================

    t.setStyle(TableStyle([

        # Fondo de la primera fila (encabezados)
        ("BACKGROUND", (0, 0), (-1, 0), colors.blueviolet),

        # Bordes alrededor de toda la tabla
        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        # Centrado vertical del contenido
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))



    # Añadimos tabla al documento
    story.append(t)

    # Renderizamos el PDF completo
    pdf.build(story)

    print("PDF de la tabla generado correctamente.")



# =====================================================================================
# BLOQUE DE EJECUCIÓN DIRECTA
# =====================================================================================
if __name__ == "__main__":
    generar_pdf_caracteristicas_parto()
