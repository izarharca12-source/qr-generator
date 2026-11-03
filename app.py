import streamlit as st
import qrcode
from datetime import datetime
import io

st.title("Generador Automático de QR por Turnos (Cada 8 Horas)")

# 1. Obtener la hora actual y calcular el bloque de 8 horas
ahora = datetime.now()
fecha_str = ahora.strftime("%Y-%m-%d")
hora_actual = ahora.hour

# Definir el turno según la hora del día (0 a 8 hrs, 8 a 16 hrs, 16 a 24 hrs)
if 0 <= hora_actual < 8:
    turno = "turno_nocturno"
    bloque_desc = "Madrugada (00:00 - 08:00)"
elif 8 <= hora_actual < 16:
    turno = "turno_matutino"
    bloque_desc = "Mañana (08:00 - 16:00)"
else:
    turno = "turno_vespertino"
    bloque_desc = "Tarde/Noche (16:00 - 24:00)"

# Token único que cambia cada 8 horas combinando fecha y turno
token_actual = f"{fecha_str}_{turno}"

# 2. Tu link de Qualtrics
url_base = "https://qualtricsxmp2wfl4t7f.qualtrics.com/jfe/form/SV_6GaFRWXENQfYMWa"
url_completa = f"{url_base}?token={token_actual}"

st.subheader(f"Fecha: {fecha_str}")
st.info(f"Bloque activo: **{bloque_desc}**")
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

# Convertir la imagen para mostrarla en Streamlit
buf = io.BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()

# 4. Mostrar en pantalla
st.image(byte_im, caption=f"Escanea para registrar asistencia - {fecha_str} ({bloque_desc})", width=350)

# Botón por si necesitas actualizar la vista manualmente
if st.button("Actualizar QR"):
    st.rerun()
