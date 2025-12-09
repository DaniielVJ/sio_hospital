from reportlab.platypus import Image, Spacer
from django.conf import settings
import os

def construir_header_logo(ancho=250): #tamaño
   

    # Ruta al logo
    ruta_logo = os.path.join(settings.BASE_DIR,"static", "images", "HermindaMartin.png")

    # Crear la imagen
    img = Image(ruta_logo)

    # Ajustar ANCHO exacto y mantener proporciones
    factor = ancho / float(img.drawWidth)
    img.drawWidth = ancho
    img.drawHeight = img.drawHeight * factor

    # Centrado
    img.hAlign = "CENTER"

    # Retornar logo + separación 
    return [
        Spacer(1, 0),  # pequeño espacio antes del logo
        img,
        Spacer(1, 20)   # espacio inferior para despegar el título
    ]
