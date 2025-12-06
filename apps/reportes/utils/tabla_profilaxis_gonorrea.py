# ============================================================================
# IMPORTACIONES NECESARIAS PARA CREAR EL PDF Y SUS TABLAS
# ============================================================================

# SimpleDocTemplate  crea el PDF completo y controla páginas, márgenes y contenido.
# Table, TableStyle = permiten construir tablas personalizadas, con bordes y colores.
# Paragraph = permite formatear texto dentro de las celdas (HTML básico).
# Spacer = crea espacios verticales entre elementos del PDF.
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# ParagraphStyle = define estilos personalizados para texto (alineación, tamaño, color).
# getSampleStyleSheet = carga estilos estándar como: Title, Heading1, Normal.
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# letter = define tamaño de página carta (muy usado en documentos de hospitales chilenos).
from reportlab.lib.pagesizes import letter

# TA_CENTER = permite centrar el texto horizontalmente dentro de Paragraph.
from reportlab.lib.enums import TA_CENTER

# colors = proporciona colores para bordes, fondos, textos, etc.
from reportlab.lib import colors



# ============================================================================
# =========================== ESTILOS PERSONALIZADOS ==========================
# ============================================================================

# Cargamos estilos base de ReportLab, que incluyen Title, Normal, BodyText, etc.
styles = getSampleStyleSheet()

# Estilo general de celdas (para datos)
cell = ParagraphStyle(
    "cell",          # Nombre interno del estilo
    fontSize=7,      # Tamaño pequeño (similar Excel)
    leading=8,       # Altura de línea entre texto
    alignment=TA_CENTER  # Centrado horizontal dentro de la celda
)

# Estilo específico para encabezados (fila superior)
header = ParagraphStyle(
    "header",
    fontSize=7,
    leading=8,
    alignment=TA_CENTER,
    textColor=colors.black  # Texto negro para buen contraste
)



# ============================================================================
# ============================= DATOS DE LA TABLA =============================
# ============================================================================

# Encabezados, basados en la tabla original del REM A11
encabezado = [
    "Total",
    "Pueblos Originarios",
    "Migrantes",
]

# Primeros y segundos valores (ambas filas tienen mismo formato)
fila_1 = ["143", "0", "7"]
fila_2 = ["143", "0", "7"]



# Convertimos encabezados y filas a Paragraph
# Sin esto, el texto NO se ajustaría a las celdas ni permitiría estilos.
encabezado = [Paragraph(x, header) for x in encabezado]
fila_1     = [Paragraph(x, cell) for x in fila_1]
fila_2     = [Paragraph(x, cell) for x in fila_2]


# Filas descriptivas largas (columna izquierda)
# Paragraph permite ajuste automático en varias líneas.
desc_1 = Paragraph(
    "Recién Nacidos vivos que reciben profilaxis ocular para gonorrea al nacer",
    cell
)

desc_2 = Paragraph(
    "Recién nacidos vivos",
    cell
)



# ============================================================================
# =========================== GENERAR PDF COMPLETO ============================
# ============================================================================

def generar_pdf_profilaxis_gonorrea():

    # Crea el PDF completo, definiendo tamaño carta
    pdf = SimpleDocTemplate("pdf/tabla_profilaxis_gonorrea.pdf", pagesize=letter)

    # story = contenedor donde se irán agregando elementos en orden
    story = []



    # ------------------------------------------------------------------------
    # TÍTULO PRINCIPAL DE LA SECCIÓN
    # ------------------------------------------------------------------------

    titulo_seccion = ParagraphStyle(
        "titulo_seccion",
        fontSize=15,      # Tamaño grande para visibilidad
        leading=24,       # Separación vertical entre líneas
        alignment=1,      # 1 significa centrado (equivalente a TA_CENTER)
        textColor=colors.HexColor("#000000"),
        spaceAfter=12     # Espacio extra bajo el título
    )

    # Creamos el título con dos partes:
    # - Nombre de la sección del REM
    # - Código “REM A 11”
    story.append(Paragraph(
        "<b>SECCIÓN D: APLICACIÓN DE PROFILAXIS OCULAR PARA GONORREA EN RECIÉN NACIDOS</b> "
        "<b>''REM A 11''</b>",
        titulo_seccion
    ))

    # Espacio entre título y tabla
    story.append(Spacer(1, 12))



    # ------------------------------------------------------------------------
    # ESTRUCTURA DE LA TABLA COMPLETA
    # ------------------------------------------------------------------------

    tabla = [
        ["", encabezado[0], encabezado[1], encabezado[2]],  # fila encabezados
        [desc_1, fila_1[0], fila_1[1], fila_1[2]],
        [desc_2, fila_2[0], fila_2[1], fila_2[2]]
    ]



    # ------------------------------------------------------------------------
    # CONFIGURACIÓN DE ANCHOS (MUY IMPORTANTE)
    # ------------------------------------------------------------------------
    # 260 px = primera columna, texto largo
    # 70 px = columnas numéricas
    total_width = 540
    col_widths = [260, 70, 70, 70]

    # Creamos la tabla con los anchos especificados
    t = Table(tabla, colWidths=col_widths)



    # ------------------------------------------------------------------------
    # APLICACIÓN DE ESTILOS VISUALES A LA TABLA
    # ------------------------------------------------------------------------

    t.setStyle(TableStyle([
        # Fondo para el encabezado superior
        ("BACKGROUND", (1,0), (-1,0), colors.salmon),

        # Color del texto en el encabezado
        ("TEXTCOLOR", (1,0), (-1,0), colors.white),

        # Bordes en toda la tabla
        ("GRID", (0,0), (-1,-1), 1, colors.black),

        # Centrado vertical
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # Añadir tabla al contenido del PDF
    story.append(t)

    # Construir el PDF final
    pdf.build(story)

    print("PDF de la tabla generado correctamente.")



# ============================================================================
# BLOQUE DE EJECUCIÓN DIRECTA DEL SCRIPT
# ============================================================================

if __name__ == "__main__":
    generar_pdf_profilaxis_gonorrea()
