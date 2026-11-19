import streamlit as st
import qrcode
from datetime import datetime
import io

st.title("ACTUALIZAR QR ANTES DE ESCANEAR")

# 1. Obtener la hora actual y calcular el bloque de 8 horas
ahora = datetime.now()
fecha_str = ahora.strftime("%Y-%m-%d")
hora_actual = ahora.hour

# Definir el turno según la hora del día (0 a 8 hrs, 8 a 16 hrs, 16 a 24 hrs)
if 6 <= hora_actual < 14:
    turno = "turno_nocturno"
    bloque_desc = "Turno 1"
elif 14 <= hora_actual < 22:
    turno = "turno_matutino"
    bloque_desc = "Turno 2"
else:
    turno = "turno_vespertino"
    bloque_desc = "Turno 3"

# Token único que cambia cada 8 horas combinando fecha y turno
token_actual = f"{fecha_str}_{turno}"

# 2. Tu link de Qualtrics
url_base = "https://qualtricsxmp2wfl4t7f.qualtrics.com/jfe/form/SV_6kWwskZMQENa3k2"
url_completa = f"{url_base}?token={token_actual}"

st.subheader(f"Fecha: {fecha_str}")
st.info(f"TURNO: **{bloque_desc}**")
st.write(f"Confirma que el turno sea el correcto")

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

# Convertir la imagen para mostrarla en Streamlit
buf = io.BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()

# 4. Mostrar en pantalla
st.image(byte_im, caption=f"Escanea para registrar asistencia - {fecha_str} ({bloque_desc})", width=350)

# Botón por si necesitas actualizar la vista manualmente
if st.button("Actualizar QR"):
    st.rerun()
