# Importamos los módulos principales de ReportLab para construir PDFs.
# SimpleDocTemplate crea el documento PDF y controla su estructura.
# Table, TableStyle permiten construir tablas profesionales con bordes, colores, spans, etc.
# Paragraph, Spacer permiten escribir texto con formato (negrita, saltos) y agregar espacios verticales.
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer



# ParagraphStyle crea estilos personalizados para los textos dentro de las celdas.
# getSampleStyleSheet carga estilos default como "Title", "Heading2", "Normal".
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# letter tamaño carta(estándar en hospitales)
from reportlab.lib.pagesizes import letter

# TA_CENTER constante para alinear texto horizontalmente.
from reportlab.lib.enums import TA_CENTER

# colors paleta de colores para fondos, texto, bordes, etc.
from reportlab.lib import colors



# ============================================================
# =============== ESTILOS PERSONALIZADOS ======================
# ============================================================

# Cargamos los estilos básicos (Title, Normal, etc.)
styles = getSampleStyleSheet()

# Estilo "cell" se usa para las celdas normales (datos)
cell = ParagraphStyle(
    "cell",        # Nombre interno del estilo
    fontSize=7,    # Tamaño de letra pequeño como en Excel
    leading=8,     # Altura de línea (evita que se superponga el texto)
    alignment=TA_CENTER  # Alineación al centro (igual que el Excel original)
)

# Estilo "header": usado exclusivamente para las celdas del encabezado.
# textColor=colors.white , convierte el texto del header en blanco.
header = ParagraphStyle(
    "header",
    fontSize=7,
    leading=8,
    alignment=TA_CENTER,
    textColor=colors.white  # Texto blanco sobre fondo de color
)



# ============================================================
# =============== DATOS DE LA TABLA ==========================
# ============================================================

# Fila completa del encabezado EXACTA al Excel.
encabezado = [
    "TIPO","TOTAL","Menos de 500","500 a 999","1.000 a 1.499",
    "1.500 a 1.999","2.000 a 2.499","2.500 a 2.999",
    "3.000 a 3.999","4.000 y más","Anomalía Congénita"
]

# Fila de valores reales sacados del Excel.
datos = ["NACIDOS VIVOS",143,0,2,2,4,16,23,82,14,1]



# ============================================================
# CONVERTIR TODAS LAS CELDAS A Paragraph
# ============================================================

# Esta conversión es CRUCIAL.
# Si no conviertes texto a Paragraph:
# no habrá autoajuste , no habrá negritas, no funcionará alineación precisa y las celdas largas NO se dividirán correctamente

encabezado = [Paragraph(str(x), header) for x in encabezado]
datos      = [Paragraph(str(x), cell) for x in datos]



# ============================================================
# =============== CREACIÓN DEL PDF ============================
# ============================================================

# Creamos el documento PDF.
# "pdf/tabla_d1.pdf" archivo generado dentro de la carpeta "pdf".
pdf = SimpleDocTemplate("pdf/tabla_d1.pdf", pagesize=letter)

# story = contenedor del contenido del documento.
# Aquí meteremos el título, espacios y la tabla.
story = []


# ============================================================
# AÑADIMOS EL TÍTULO SUPERIOR DEL DOCUMENTO
# ============================================================

# Paragraph permite usar HTML básico: <b> para negrita.
story.append(
    Paragraph(
        "<b>SECCIÓN D.1: INFORMACIÓN GENERAL DE RECIÉN NACIDOS VIVOS</b> "
        "<b> ''REM A 24'' </b>", 
        styles["Title"]   # estilo de título predefinido
    )
)

# Spacer crea espacio vertical entre elementos , es equivalente a "margin-top".
story.append(Spacer(1, 12))



# ============================================================
# ============== ARMAR ESTRUCTURA DE LA TABLA =================
# ============================================================

# Componemos la tabla con dos filas:
# fila 0: encabezado
# fila 1: datos
tabla = [encabezado, datos]



# ============================================================
# ANCHOS DE COLUMNA (ESTRATÉGICOS)
# ============================================================

# ancho_total=540 ,  corresponde al ancho útil dentro de la página en carta.
# Dividimos el ancho total en partes iguales.
ancho_total = 540
col = ancho_total / len(encabezado)

# Construimos la tabla con colWidths dinámicos.
#colWidths define el ancho de CADA columna
t = Table(tabla, colWidths=[col]*len(encabezado))



# ============================================================
# =============== ESTILOS VISUALES DE LA TABLA ===============
# ============================================================

t.setStyle(TableStyle([
    
    # Coloreamos el encabezado (solo la primera fila)
    ("BACKGROUND", (0, 0), (-1, 0), colors.red),

    # Color del texto del encabezado (aunque declaramos blanco en el estilo
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),

    # Dibujar bordes en toda la tabla
    ("GRID", (0, 0), (-1, -1), 1, colors.black),

    # Especificar la fuente usada
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

    # Tamaño de texto  aunque ya está en ParagraphStyle por seguridad lo reafirmamos
    ("FONTSIZE", (0, 0), (-1, -1), 7),

    # Alineación de contenido centrado ( es útil para números)
    ("ALIGN", (1, 1), (-1, -1), "CENTER")
]))



# Agregamos la tabla al contenido
story.append(t)

# Construimos finalmente el PDF
pdf.build(story)

print("PDF de la tabla generado correctamente.")
