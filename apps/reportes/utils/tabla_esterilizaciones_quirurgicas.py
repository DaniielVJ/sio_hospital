# =====================================================================================
# 1. IMPORTACIONES NECESARIAS PARA GENERAR EL PDF CON TABLA
# =====================================================================================

# SimpleDocTemplate:
#   - Es la clase que crea el documento PDF.
#   - Define el tamaño de la hoja, márgenes y recibe una lista de elementos (story).
# Table:
#   - Permite crear tablas con filas y columnas.
# TableStyle:
#   - Permite aplicar estilos a la tabla (colores, bordes, fusiones, etc.).
# Paragraph:
#   - Permite escribir texto con formato (por ejemplo <b>negrita</b>) dentro de una celda.
# Spacer:
#   - Inserta espacio vertical entre elementos (como margen superior o separación de secciones).
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# ParagraphStyle:
#   - Define estilos de texto personalizados (tamaño, color, alineación).
# getSampleStyleSheet:
#   - Carga una colección de estilos base, como "Title", "Normal", etc., para reutilizarlos.
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# TA_CENTER:
#   - Constante usada para indicar alineación horizontal centrada en ParagraphStyle.
from reportlab.lib.enums import TA_CENTER

# letter:
#   - Constante que indica el tamaño de página "carta" (Letter: 8.5 x 11 pulgadas).
from reportlab.lib.pagesizes import letter

# colors:
#   - Módulo con colores predefinidos (black, white, khaki, lightgrey, etc.).
from reportlab.lib import colors



# =====================================================================================
# 2. DEFINICIÓN DE ESTILOS DE TEXTO
# =====================================================================================

# Cargamos los estilos base de ReportLab (Title, Normal, BodyText, etc.)
styles = getSampleStyleSheet()

# Estilo para las celdas de datos (números y textos cortos) centrados.
cell_center = ParagraphStyle(
    "cell_center",   # Nombre interno del estilo
    fontSize=8,      # Tamaño de letra pequeño para similitud con Excel
    leading=10,      # Altura de línea (distancia vertical entre líneas de texto)
    alignment=TA_CENTER  # Alineación horizontal centrada
)

# Estilo para los encabezados de columnas.
# Usamos un tamaño un poco más grande para destacar sobre los datos.
header_center = ParagraphStyle(
    "header_center",
    fontSize=9,       # Un poco más grande que los datos
    leading=11,       # Leve aumento de altura de línea para legibilidad
    alignment=TA_CENTER,
    textColor=colors.black  # Texto negro (contraste alto sobre fondo claro)
)



# =====================================================================================
# 3. DEFINICIÓN DE LOS ENCABEZADOS (2 NIVELES)
# =====================================================================================

# Primer nivel (fila 0)
# Esta fila contiene los títulos agrandados:
#   - "SEXO"
#   - "TOTAL"
#   - "EDAD (en años)" = abarca 3 columnas (Menor de 20 / 20-34 / 35+)
#   - "Trans" = abarca 2 columnas (Masculino / Femenino)
encabezado_superior = [
    Paragraph("<b>SEXO</b>", header_center),          # Columna 0
    Paragraph("<b>TOTAL</b>", header_center),         # Columna 1
    Paragraph("<b>EDAD (en años)</b>", header_center),# Columna 2 (se fusiona con 3 y 4)
    "",                                              # Columna 3 (parte de la fusión EDAD)
    "",                                              # Columna 4 (parte de la fusión EDAD)
    Paragraph("<b>Trans</b>", header_center),        # Columna 5 (se fusiona con 6)
    "",                                              # Columna 6 (parte de la fusión Trans)
]

# Segundo nivel (fila 1)
# Aquí se especifican los subtítulos bajo EDAD (en años) y Trans.
encabezado_inferior = [
    "",  # Debajo de "SEXO" (no tiene subtítulo propio)
    "",  # Debajo de "TOTAL" (tampoco subtítulo)
    Paragraph("<b>Menor<br/>de 20 años</b>", header_center),  # Subcolumna EDAD 1
    Paragraph("<b>20 - 34 años</b>", header_center),          # Subcolumna EDAD 2
    Paragraph("<b>35 y más años</b>", header_center),         # Subcolumna EDAD 3
    Paragraph("<b>Masculino</b>", header_center),             # Subcolumna Trans 1
    Paragraph("<b>Femenino</b>", header_center),              # Subcolumna Trans 2
]



# =====================================================================================
# 4. FILAS DE DATOS (MUJER / HOMBRE)
# =====================================================================================

# Datos tal cual aparecen en el Excel:
# MUJER: TOTAL 33, Menor 20 = 0, 20-34 = 19, 35+ = 14, Trans Masc = 0, Trans Fem = 0
# HOMBRE: TOTAL 0, todo lo demás 0 (vacío)
datos = [
    ["MUJER",  "33", "0", "19", "14", "0", "0"],
    ["HOMBRE", "0",  "0", "0",  "0",  "0", "0"],
]

# Convertimos cada valor a Paragraph con el estilo centrado,
# para asegurarnos:
#   - alineación correcta
#   - compatibilidad con estilos y saltos de línea
filas = [
    [Paragraph(str(x), cell_center) for x in fila]
    for fila in datos
]



# =====================================================================================
# 5. FUNCIÓN PRINCIPAL QUE GENERA EL PDF DE ESTA TABLA
# =====================================================================================

def generar_pdf_esterilizaciones_quirurgicas():

    # Creamos el documento PDF:
    #   - "pdf/tabla_esterilizaciones.pdf" = ruta donde se guardará.
    #   - pagesize=letter = tamaño carta.
    pdf = SimpleDocTemplate("pdf/tabla_esterilizaciones.pdf", pagesize=letter)

    # "story" es la lista de elementos que van a ir apareciendo en orden dentro del PDF.
    story = []

    # -----------------------------------------------------------------------------
    # 5.1 TÍTULO PRINCIPAL DE LA SECCIÓN
    # -----------------------------------------------------------------------------

    # Agregamos el título principal usando el estilo "Title" que ya viene con ReportLab.
    story.append(
        Paragraph("<b>SECCIÓN G: ESTERILIZACIONES QUIRÚRGICAS</b>", styles["Title"])
    )

    # Insertamos un espacio de 12 puntos debajo del título para separar visualmente.
    story.append(Spacer(1, 12))


    # -----------------------------------------------------------------------------
    # 5.2 CONSTRUCCIÓN LÓGICA DE LA TABLA
    # -----------------------------------------------------------------------------

    # La tabla completa está formada por:
    #   - fila 0 = encabezado_superior
    #   - fila 1 = encabezado_inferior
    #   - filas 2 y 3 = MUJER y HOMBRE
    tabla = [
        encabezado_superior,
        encabezado_inferior,
    ] + filas  # Concatena las filas de datos al final



    # -----------------------------------------------------------------------------
    # 5.3 ANCHOS DE COLUMNA
    # -----------------------------------------------------------------------------

    # Definimos los anchos de las 7 columnas.
    # Puedes ajustar estos valores para que se parezca lo máximo posible al Excel.
    col_widths = [80, 60, 80, 80, 80, 80, 80]

    # Creamos el objeto Table de ReportLab con los anchos definidos.
    t = Table(tabla, colWidths=col_widths)



    # -----------------------------------------------------------------------------
    # 5.4 ESTILOS VISUALES DE LA TABLA
    # -----------------------------------------------------------------------------

    t.setStyle(TableStyle([

        # Fondo gris claro para la fila de encabezado superior
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),

        # Fondo amarillo suave para la fila de encabezado inferior
        ("BACKGROUND", (0, 1), (-1, 1), colors.lightgreen),

        # Dibujar una grilla (bordes) alrededor de todas las celdas
        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        # FUSIÓN DE CELDAS:
        #   ("SPAN", (col_inicio, fila_inicio), (col_final, fila_final))
        # "EDAD (en años)" ocupa las columnas 2, 3 y 4 en la fila 0
        ("SPAN", (2, 0), (4, 0)),

        # "Trans" ocupa las columnas 5 y 6 en la fila 0
        ("SPAN", (5, 0), (6, 0)),

        # Centrado vertical de todo el contenido
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))



    # -----------------------------------------------------------------------------
    # 5.5 AÑADIR TABLA AL DOCUMENTO Y GENERAR EL PDF
    # -----------------------------------------------------------------------------

    # Agregamos la tabla al flujo del PDF
    story.append(t)

    # Construimos el PDF con todo lo acumulado en "story"
    pdf.build(story)

    print("PDF de la tabla generado correctamente.")



# =====================================================================================
# 6. BLOQUE DE EJECUCIÓN DIRECTA
# =====================================================================================

# Este bloque se ejecuta SOLO si se corre este archivo directamente:
#   python este_archivo.py
# Si importas esta función desde otro archivo, este bloque NO se ejecuta,
# lo que permite reutilizar generar_pdf_esterilizaciones() sin que se genere
# el PDF automáticamente.
if __name__ == "__main__":
    generar_pdf_esterilizaciones_quirurgicas()
