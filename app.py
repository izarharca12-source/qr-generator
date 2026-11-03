import streamlit as st
import qrcode
from datetime import datetime
import io

st.title("Generador Automático de QR por Turno/Fecha")

# 1. Obtener fecha actual
ahora = datetime.now()
fecha_str = ahora.strftime("%Y-%m-%d")

# 2. Tu link de Qualtrics
url_base = "https://tu-encuesta.qualtrics.com/jfe/form/SV_tuEncuestaID"
token_actual = f"{fecha_str}"
url_completa = f"{url_base}?token={token_actual}"

st.subheader(f"QR Activo para hoy: {fecha_str}")
st.write(f"Enlace oculto en el QR: `{url_completa}`")

# 3. Generar la imagen del QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url_completa)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Convertir la imagen para mostrarla correctamente en Streamlit
buf = io.BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()

# 4. Mostrar en pantalla de Streamlit
st.image(byte_im, caption=f"Escanea para registrar asistencia - {fecha_str}", width=350)
