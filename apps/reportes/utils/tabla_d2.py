# ===================================================================
# IMPORTACIONES DE REPORTLAB Y ESTILOS NECESARIOS
# ===================================================================

# SimpleDocTemplate => Crea el PDF final, define tamaño de hoja, márgenes, etc.
# Table, TableStyle => Permiten construir tablas profesionales con bordes, colores y estructura.
# Paragraph, Spacer => Paragraph permite textos con formato HTML. Spacer agrega espacios verticales.
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# ParagraphStyle => Permite crear estilos personalizados para textos dentro de celdas.
# getSampleStyleSheet => Obtiene estilos por defecto: Title, Normal, Heading1, etc.
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# Tamaño de la hoja tipo carta estándar.
from reportlab.lib.pagesizes import letter

# Alineación horizontal del texto (al centro en este caso).
from reportlab.lib.enums import TA_CENTER

# Colores predefinidos y HEX para fondo, texto y bordes.
from reportlab.lib import colors



# ===================================================================
# ESTILOS PERSONALIZADOS PARA CELDAS
# ===================================================================

styles = getSampleStyleSheet()   # Carga estilos estándar (Title, Heading2, etc.)

# Estilo para celdas normales (cuerpo de la tabla).
cell = ParagraphStyle(
    "cell",           # Nombre interno del estilo
    fontSize=7,       # Tamaño pequeño, igual a Excel
    leading=8,        # Espaciado entre líneas
    alignment=TA_CENTER
)

# Estilo para celdas del encabezado.
header = ParagraphStyle(
    "header",
    fontSize=7,
    leading=8,
    alignment=TA_CENTER,
    textColor=colors.white  # Texto blanco (contraste con fondo coral del encabezado superior)
)



# ===================================================================
# ENCABEZADOS NIVEL 1 (Fila superior)
# ===================================================================
# Esta es la fila donde algunos conceptos se repiten porque abarcan varias columnas:
# Ej: PROFILAXIS => Hepatitis B / Ocular
# TIPO DE PARTO => 3 columnas

encabezado_n1 = [
    "TIPO",
    "PROFILAXIS",
    "PROFILAXIS",
    "TIPO DE PARTO",
    "TIPO DE PARTO",
    "TIPO DE PARTO",
    "APGAR",
    "APGAR",
    "Reanimación Básica",
    "Reanimación Avanzada",
    "EHI Grado II y III",
]

# ===================================================================
# ENCABEZADOS NIVEL 2 (Fila inferior del encabezado)
# ===================================================================
# Aquí se distribuyen los “subtítulos” de cada grupo.
# Por ejemplo:
# PROFILAXIS → Hepatitis B / Ocular

encabezado_n2 = [
    "",                    # Debajo de TIPO
    "Hepatitis B",
    "Ocular",
    "Parto Vaginal",
    "Parto Instrumental",
    "Cesárea",
    "Parto extrahospitalario",
    "Apgar ≤ 3 al minuto",
    "Apgar ≤ 6 a los 5 minutos",
    "",                    # Reanimación básica → ya está nombrado arriba
    "",                    # Reanimación avanzada → igual
]



# ===================================================================
# SECCIÓN INFERIOR (TABLA CHICA DE PARTOS)
# ===================================================================
# Esta tabla contiene valores separados y no forma parte de la tabla principal.
tabla_inferior = [
    ["DISTOCICO", Paragraph("1", cell)],
    ["VACUUM", Paragraph("3", cell)],
    ["C. URGENCIA", Paragraph("39", cell)],
    ["C. ELECTIVA", Paragraph("27", cell)],
    ["TOTAL DE PARTOS", Paragraph("143", cell)],
]



# ===================================================================
# CONVERTIR LOS ENCABEZADOS A Paragraph
# ===================================================================
# Esto es obligatorio para que:
# - El texto pueda ajustarse dentro de celdas
# - Se respete alineación y estilo
# - Se permitan saltos de línea, etiquetas HTML, etc.

encabezado_n1 = [Paragraph(x, header) for x in encabezado_n1]
encabezado_n2 = [Paragraph(x, cell) for x in encabezado_n2]



# ===================================================================
# DATOS PRINCIPALES DE LA TABLA D.2
# ===================================================================

fila = [
    "NACIDOS VIVOS",
    143, 143, 73, 4, 66, 0, 3, 3, 16, 6
]

# Convertimos fila a Paragraphs para aplicar estilo uniforme
fila = [Paragraph(str(x), cell) for x in fila]
















# ===================================================================
# FUNCIÓN PARA GENERAR EL PDF COMPLETO
# ===================================================================

def generar_pdf_tabla_d2():

    # Creamos el PDF donde se incluirá la tabla D.2.
    pdf = SimpleDocTemplate("pdf/tabla_d2.pdf", pagesize=letter)

    story = []  # Lista de elementos que tendrá el PDF



    # TÍTULO PRINCIPAL DEL PDF
    story.append(
        Paragraph(
            "<b>SECCIÓN D.2: ATENCIÓN INMEDIATA DEL RECIÉN NACIDO</b><br/>"
            "<b>''REM A 24''</b>",
            styles["Title"]  # Estilo de título por defecto
        )
    )

    # Espacio entre título y tabla
    story.append(Spacer(1, 12))



    # ===================================================================
    # ARMAMOS LA TABLA PRINCIPAL (NIVEL 1, NIVEL 2, FILA DE DATOS)
    # ===================================================================

    tabla1 = [
        encabezado_n1,  # Fila 1
        encabezado_n2,  # Fila 2
        fila            # Fila de datos
    ]

    # Ancho total de la tabla dividido en columnas iguales
    ancho_total = 540
    col = ancho_total / len(encabezado_n1)

    t1 = Table(tabla1, colWidths=[col] * len(encabezado_n1))

    # ===================================================================
    # ESTILOS DE LA TABLA PRINCIPAL
    # ===================================================================

    t1.setStyle(TableStyle([

        # Fondo del ENCABEZADO NIVEL 1 (coral)
        ("BACKGROUND", (0,0), (-1,0), colors.coral),

        # Fondo del ENCABEZADO NIVEL 2 (gris claro)
        ("BACKGROUND", (0,1), (-1,1), colors.lightgrey),

        # Bordes de toda la tabla
        ("GRID", (0,0), (-1,-1), 1, colors.black),

        # Alineación vertical centrada
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    story.append(t1)



    # Espacio antes de la tabla inferior
    story.append(Spacer(1, 30))



    # ===================================================================
    # TABLA INFERIOR (DISTÓCICO, VACUUM, ETC.)
    # ===================================================================

    tabla2 = Table(tabla_inferior, colWidths=[200, 80])

    tabla2.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
    ]))

    story.append(tabla2)



    # Generar finalmente el PDF
    pdf.build(story)
    print("PDF de la tabla generado correctamente.")



# ===================================================================
# EJECUCIÓN DIRECTA DEL SCRIPT
# ===================================================================

if __name__ == "__main__":
    generar_pdf_tabla_d2()
