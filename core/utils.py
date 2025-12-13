import random
from datetime import datetime

def generar_codigo_temporal():
    """
    Genera un código temporal único para pacientes sin documento.
    Ejemplo: TMP-2025-11-20-483920
    """
    fecha = datetime.now().strftime("%Y%m%d")
    rnd = random.randint(100000, 99999999999999999999)
    return f"TMP-{fecha}-{rnd}"


