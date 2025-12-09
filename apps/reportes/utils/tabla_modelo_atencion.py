import io
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from apps.reportes.utils.pdf_header import construir_header_logo



# =====================================================================================
# FUNCIÓN PARA GENERAR PDF EN BUFFER
# =====================================================================================
def crear_tabla_modelo_atencion_buffer():

    # ------------------ ESTILOS ------------------
    styles = getSampleStyleSheet()

    cell_left = ParagraphStyle(
        "cell_left",
        fontSize=7,
        leading=9,
        alignment=TA_LEFT
    )

    cell_center = ParagraphStyle(
        "cell_center",
        fontSize=7,
        leading=9,
        alignment=TA_CENTER
    )

    header_center = ParagraphStyle(
        "header_center",
        fontSize=8,
        leading=10,
        alignment=TA_CENTER,
        textColor=colors.black
    )


    # ------------------ ENCABEZADO ------------------
    encabezado = [
        "",
        Paragraph("<b>TOTAL</b>", header_center),
        Paragraph("<b>&lt;28 semanas</b>", header_center),
        Paragraph("<b>28 a 37 semanas</b>", header_center),
        Paragraph("<b>38 semanas y más</b>", header_center),
    ]


    # ------------------ TABLA COMPLETA ------------------
    tabla = [
        encabezado,

        [Paragraph("ESPONTANEO", cell_left), "57", "1", "20", "36"],

        [Paragraph("INDUCIDOS", cell_left), "", "", "", ""],
        ["      MECÁNICA", "0", "0", "0", "0"],
        ["      FARMACOLÓGICA", "20", "0", "4", "16"],

        [Paragraph("CONDUCCIÓN OXITÓCICA", cell_left), "68", "1", "20", "50"],
        [Paragraph("LIBERTAD DE MOVIMIENTO", cell_left), "65", "1", "20", "46"],
        [Paragraph("RÉGIMEN HÍDRICO AMPLIO", cell_left), "56", "0", "17", "42"],

        [Paragraph("Manejo del dolor", cell_left), "", "", "", ""],
        ["      No farmacológico", "40", "0", "10", "30"],
        ["      Farmacológico", "39", "0", "9", "30"],

        [Paragraph("POSICIÓN AL MOMENTO DEL EXPULSIVO", cell_left), "", "", "", ""],
        ["      LITOTOMÍA", "1", "1", "", ""],
        ["      OTRAS POSICIONES", "103", "0", "29", "74"],

        [Paragraph("EPISIOTOMIA", cell_left), "0", "0", "0", "0"],

        [Paragraph("ACOMPAÑAMIENTO", cell_left), "", "", "", ""],
        ["      DURANTE EL TRABAJO DE PARTO", "64", "0", "19", "47"],
        ["      SOLO EN EL EXPULSIVO", "68", "0", "22", "48"],
    ]


    # ------------------ ANCHOS DE COLUMNA ------------------
    col_widths = [250, 60, 70, 70, 70]


    # ------------------ CREAR BUFFER ------------------
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter, topMargin=30)

    story = []

    story.extend(construir_header_logo())

    # TÍTULO
    story.append(
        Paragraph("<b>CARACTERISTICAS DEL MODELO DE ATENCIÓN</b>", styles["Title"])
    )
    story.append(Spacer(1, 10))


    # ------------------ TABLA REPORTLAB ------------------
    t = Table(tabla, colWidths=col_widths)

    t.setStyle(TableStyle([
        ("BACKGROUND", (1, 0), (-1, 0), colors.lightblue),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    story.append(t)

    # Construir PDF
    pdf.build(story)
    buffer.seek(0)

    return buffer



# -----------------------------------------------------------------------
# PRUEBA LOCAL OPCIONAL
# -----------------------------------------------------------------------
if __name__ == "__main__":
    buf = crear_tabla_modelo_atencion_buffer()
    with open("tabla_modelo_atencion_buffer.pdf", "wb") as f:
        f.write(buf.read())
    print("PDF generado correctamente.")
