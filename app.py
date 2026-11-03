import qrcode
from datetime import datetime
from IPython.display import display, Image

# 1. Obtener fecha actual y armar la URL con el token de Qualtrics
ahora = datetime.now()
fecha_str = ahora.strftime("%Y-%m-%d")

url_base = "https://tu-encuesta.qualtrics.com/jfe/form/SV_tuEncuestaID"
url_completa = f"{url_base}?token={fecha_str}"

print(f"--- QR ACTIVO PARA HOY: {fecha_str} ---")
print(f"Enlace integrado: {url_completa}")

# 2. Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url_completa)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
nombre_archivo = f"qr_{fecha_str}.png"
img.save(nombre_archivo)

# 3. Mostrar la imagen directamente aquí abajo en la celda de Colab
display(Image(nombre_archivo))
