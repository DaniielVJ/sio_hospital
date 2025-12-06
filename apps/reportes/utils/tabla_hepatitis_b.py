# =====================================================================
# IMPORTACIONES PRINCIPALES DE REPORTLAB PARA CREAR EL PDF Y TABLAS
# =====================================================================

# SimpleDocTemplate  Crea un documento PDF, controla tamaño, márgenes y contenido.
# Table, TableStyle  Construyen tablas profesionales y permiten agregar estilos visuales.
# Paragraph  Permite usar texto con formato HTML (<b>, <br/>) dentro de las celdas.
# Spacer  Inserta espacios verticales entre bloques del PDF.
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# ParagraphStyle  Crea estilos personalizados para el texto dentro de celdas.
# getSampleStyleSheet  Provee estilos predeterminados como Title, Heading1, Normal.
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# letter  Tamaño de página tipo carta (utilizado en muchos hospitales en Chile).
from reportlab.lib.pagesizes import letter

# TA_CENTER Constante usada para alinear el texto horizontalmente al centro.
from reportlab.lib.enums import TA_CENTER

# colors → Permite usar colores predefinidos o Hex ej. "#FF0000".
from reportlab.lib import colors



# =====================================================================
# ====================== DEFINICIÓN DE ESTILOS =========================
# =====================================================================

# Carga un set de estilos predeterminados de ReportLab como "Title".
styles = getSampleStyleSheet()

# Estilo para el contenido de celdas (datos)
cell = ParagraphStyle(
    "cell",
    fontSize=7,       # Tamaño de letra pequeño para simular formato Excel
    leading=8,        # Altura de línea para evitar que el texto se pegue entre sí
    alignment=TA_CENTER  # Centrado horizontal
)

# Estilo para encabezados de la tabla
header = ParagraphStyle(
    "header",
    fontSize=7,
    leading=8,
    alignment=TA_CENTER,
    textColor=colors.black  # Texto negro para alto contraste sobre fondo claro
)



# =====================================================================
# ====================== DATOS DEL ENCABEZADO ==========================
# =====================================================================

# Las columnas presentes en el Excel
encabezado = [
    "Total",
    "Pueblos Originarios",
    "Migrantes",
]

# Fila 1 y fila 2 de datos, tomadas del Excel original
fila_1 = ["0", "0", "0"]
fila_2 = ["0", "0", "0"]



# =====================================================================
# ===== CONVERTIMOS LOS ENCABEZADOS Y FILAS A Paragraph AUTOMÁTICO =====
# =====================================================================

# Convertimos el texto en Paragraph para:
# permitir saltos de línea si fuese necesario
# aplicar estilos correctamente
# evitar desbordes cuando una celda tiene texto largo
encabezado = [Paragraph(x, header) for x in encabezado]
fila_1     = [Paragraph(x, cell) for x in fila_1]
fila_2     = [Paragraph(x, cell) for x in fila_2]



# =====================================================================
# DESCRIPCIONES LARGAS DE CADA FILA (COLUMNA IZQUIERDA)
# =====================================================================

# Estas celdas contienen descripciones extensas → usamos Paragraph para ajuste automático
desc_1 = Paragraph(
    "Recién nacidos hijos de madre Hepatitis B positiva, nacidos en el periodo",
    cell  # estilo sencillo y centrado
)

desc_2 = Paragraph(
    "Recién nacidos hijos de madre Hepatitis B positiva que recibieron profilaxis completa, según la normativa vigente",
    cell
)



# =====================================================================
# FUNCIÓN PRINCIPAL PARA GENERAR EL PDF
# =====================================================================

def generar_pdf_hepatitis_b():

    # Creamos el documento PDF donde se insertará la tabla.
    pdf = SimpleDocTemplate(
        "pdf/tabla_hepatitis_b.pdf",
        pagesize=letter  # tamaño carta
    )

    story = []  # Lista donde se almacenan todos los elementos que se agregarán al PDF.



    # =====================================================================
    # TÍTULO PRINCIPAL DE LA SECCIÓN (EN NEGRITA Y GRANDE)
    # =====================================================================

    # Estilo personalizado para el título superior
    titulo_seccion = ParagraphStyle(
        "titulo_seccion",
        fontSize=15,        # Título grande
        leading=24,         # Espacio entre líneas
        alignment=1,        # 1 = centrado (equivalente a TA_CENTER)
        textColor=colors.HexColor("#000000"),
        spaceAfter=12       # Espacio debajo del título
    )

    # Agregamos el título con negritas HTML
    story.append(Paragraph(
        "<b>SECCIÓN J: PROFILAXIS DE TRANSMISIÓN VERTICAL APLICADA AL RECIÉN NACIDO, "
        "HIJO DE MADRE HEPATITIS B POSITIVA</b> <b>''REM A 11''</b>",
        titulo_seccion
    ))

    # Separador entre el título y la tabla
    story.append(Spacer(1, 12))



    # =====================================================================
    # CONSTRUCCIÓN DE LA TABLA PRINCIPAL
    # =====================================================================

    # Estructura de la tabla:
    # - La primera celda de la primera fila va vacía (columna de descripciones)
    # - Luego se agregan los encabezados convertidos a Paragraph
    tabla = [
        ["", encabezado[0], encabezado[1], encabezado[2]],
        [desc_1, fila_1[0], fila_1[1], fila_1[2]],
        [desc_2, fila_2[0], fila_2[1], fila_2[2]]
    ]



    # =====================================================================
    # ANCHOS DE COLUMNA (MUY IMPORTANTE)
    # =====================================================================

    # 260 px  columna de texto largo
    # 70 px por cada columna numérica
    col_widths = [260, 70, 70, 70]

    # Construcción del objeto Table de ReportLab
    t = Table(tabla, colWidths=col_widths)



    # =====================================================================
    # ESTILOS VISUALES DE LA TABLA
    # =====================================================================

    t.setStyle(TableStyle([

        # Fondo amarillo claro SOLO en la fila de encabezado
        ("BACKGROUND", (1, 0), (-1, 0), colors.limegreen),

        # Bordes de toda la tabla
        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        # Centrado vertical en todas las celdas
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))



    # Añadimos la tabla a la lista
    story.append(t)

    # Generamos finalmente el PDF
    pdf.build(story)

    print("PDF de la tabla generado correctamente.")



# =====================================================================
# BLOQUE DE EJECUCIÓN DIRECTA
# =====================================================================

if __name__ == "__main__":
    generar_pdf_hepatitis_b()
