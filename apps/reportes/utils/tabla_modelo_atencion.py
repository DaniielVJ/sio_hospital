# =====================================================================================
# IMPORTACIONES NECESARIAS PARA CREAR PDF CON REPORTLAB
# =====================================================================================

# SimpleDocTemplate = estructura base del PDF (controla página, márgenes y contenido).
# Table = permite crear tablas con filas y columnas.
# TableStyle = sirve para aplicar colores, bordes, alineación y otros estilos.
# Paragraph = permite agregar texto con formato HTML (negritas, saltos, sangría).
# Spacer = agrega espacios verticales entre elementos (título, tablas, etc.)
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# ParagraphStyle = define estilos tipográficos personalizados (tamaño, alineación).
# getSampleStyleSheet = carga estilos por defecto (Title, Normal, etc.).
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# letter = establece tamaño carta (8.5x11").
from reportlab.lib.pagesizes import letter

# TA_CENTER, TA_LEFT = constantes para indicar alineación.
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# colors = paleta de colores para usar en la tabla.
from reportlab.lib import colors



# =====================================================================================
# DEFINICIÓN DE ESTILOS PERSONALIZADOS
# =====================================================================================

# Cargamos los estilos base para usar "Title", "Normal", etc.
styles = getSampleStyleSheet()

# Estilo para celdas alineadas a la izquierda (texto largo descriptivo).
cell_left = ParagraphStyle(
    "cell_left",
    fontSize=7,      # Tamaño pequeño (similar al Excel)
    leading=9,       # Espaciado entre líneas dentro de la celda
    alignment=TA_LEFT
)

# Estilo para celdas centradas (números en columnas a la derecha).
cell_center = ParagraphStyle(
    "cell_center",
    fontSize=7,
    leading=9,
    alignment=TA_CENTER
)

# Estilo para encabezados de columna.
header_center = ParagraphStyle(
    "header_center",
    fontSize=8,      # Más grande para diferenciar encabezado
    leading=10,
    alignment=TA_CENTER,
    textColor=colors.black
)








# =====================================================================================
# FUNCIÓN PRINCIPAL QUE GENERA EL PDF DE ESTA TABLA
# =====================================================================================

def generar_pdf_modelo_atencion():

    # Creamos el documento PDF con tamaño carta.
    pdf = SimpleDocTemplate("pdf/tabla_modelo_atencion.pdf", pagesize=letter)

    # Lista donde se irán agregando los elementos (título, tabla, etc.)
    story = []



    # =================================================================================
    # TÍTULO PRINCIPAL DE LA SECCIÓN
    # =================================================================================

    story.append(
        Paragraph("<b>CARACTERISTICAS DEL MODELO DE ATENCION</b>", styles["Title"])
    )

    # Agregamos espacio entre el título y la tabla.
    story.append(Spacer(1, 10))



    # =================================================================================
    # ENCABEZADO DE LA TABLA
    # =================================================================================

    # Primera celda del encabezado es vacía, porque esa columna es la de categorías.
    encabezado = [
        "",  
        Paragraph("<b>TOTAL</b>", header_center),
        Paragraph("<b>&lt;28 semanas</b>", header_center),
        Paragraph("<b>28 a 37 semanas</b>", header_center),
        Paragraph("<b>38 semanas y más</b>", header_center),
    ]



    # =================================================================================
    # CONSTRUCCIÓN DE TODAS LAS FILAS DE LA TABLA
    # =================================================================================

    tabla = [

        # Encabezado completo
        encabezado,

        # ---- GRUPO 1: ESPONTÁNEO ----
        [Paragraph("ESPONTANEO", cell_left), "57", "1", "20", "36"],

        # ---- GRUPO 2: INDUCIDOS ----
        [Paragraph("INDUCIDOS", cell_left), "", "", "", ""],   # Fila contenedora
        ["      MECÁNICA",       "0",  "0",  "0",  "0"],        # Subfila con sangría
        ["      FARMACOLÓGICA",  "20", "0",  "4", "16"],        # Subfila

        # ---- GRUPO 3 ----
        [Paragraph("CONDUCCIÓN OXITÓCICA", cell_left), "68", "1", "20", "50"],
        [Paragraph("LIBERTAD DE MOVIMIENTO", cell_left), "65", "1", "20", "46"],
        [Paragraph("RÉGIMEN HÍDRICO AMPLIO", cell_left), "56", "0", "17", "42"],

        # ---- GRUPO 4: Manejo del dolor ----
        [Paragraph("Manejo del dolor", cell_left), "", "", "", ""],
        ["      No farmacológico", "40", "0", "10", "30"],
        ["      Farmacológico",   "39", "0", "9", "30"],

        # ---- GRUPO 5: Posición del expulsivo ----
        [Paragraph("POSICIÓN AL MOMENTO DEL EXPULSIVO", cell_left), "", "", "", ""],
        ["      LITOTOMÍA",       "1", "1", "", ""],
        ["      OTRAS POSICIONES", "103", "0", "29", "74"],

        # ---- GRUPO 6 ----
        [Paragraph("EPISIOTOMIA", cell_left), "0", "0", "0", "0"],

        # ---- GRUPO 7: Acompañamiento ----
        [Paragraph("ACOMPAÑAMIENTO", cell_left), "", "", "", ""],
        ["      DURANTE EL TRABAJO DE PARTO", "64", "0", "19", "47"],
        ["      SOLO EN EL EXPULSIVO",        "68", "0", "22", "48"],
    ]



    # =================================================================================
    # DEFINICIÓN DE ANCHOS DE COLUMNA
    # =================================================================================
    # Columna 1 = 250 px (texto)
    # Columnas de números = 60-70 px cada una
    col_widths = [250, 60, 70, 70, 70]



    # =================================================================================
    # CREACIÓN DE LA TABLA CON REPORTLAB
    # =================================================================================

    t = Table(tabla, colWidths=col_widths)



    # =================================================================================
    # ESTILOS VISUALES APLICADOS A LA TABLA
    # =================================================================================

    t.setStyle(TableStyle([

        # Color de fondo solo para los encabezados numéricos
        ("BACKGROUND", (1, 0), (-1, 0), colors.lightblue),

        # Líneas de cuadrícula para toda la tabla
        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        # Ajuste vertical de contenido (centro)
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))



    # Agregar tabla al contenido del PDF
    story.append(t)

    # Construir archivo final
    pdf.build(story)

    print("PDF generado correctamente.")



# =====================================================================================
# BLOQUE DE EJECUCIÓN DIRECTA DEL SCRIPT
# =====================================================================================
if __name__ == "__main__":
    generar_pdf_modelo_atencion()
