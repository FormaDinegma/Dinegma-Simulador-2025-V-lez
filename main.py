import streamlit as st

# --- TABLAS DE COMISIONES ---
# --- CLASIFICACIÓN DE TIENDAS VÉLEZ ---

TIENDAS_VELEZ = {
    "Vélez Oakland 1": "A",
    "Vélez Oakland 2": "A",
    "Vélez Miraflores": "A",
    "Vélez Cayalá": "A",
    "Vélez Multiplaza": "A",
    "Vélez Naranjo": "B",
    "Vélez Portales": "B",
    "Vélez Chimaltenango": "B",
    "Vélez Pradera Xela": "B",
    "Vélez Interplaza Xela": "B",
    "Vélez Kiosco Miraflores": "Kiosco",
    "Vélez Kiosco Oakland": "Kiosco",
    "Vélez Kiosco Decima": "Kiosco",
    "Vélez Kiosco Gran Vía": "Kiosco",
    "Vélez Kiosco Galerias": "Kiosco"
}

# ADMINISTRADORES - TIENDA A
comisiones_admins_A = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0044},
        {"rango": (90, 99.99), "variable": 0.0050},
        {"rango": (100, 109.99), "variable": 0.0069},
        {"rango": (110, 119.99), "variable": 0.0072},
        {"rango": (120, 999), "variable": 0.0076},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0006},
        {"rango": (90, 99.99), "variable": 0.0007},
        {"rango": (100, 109.99), "variable": 0.0010},
        {"rango": (110, 119.99), "variable": 0.0010},
        {"rango": (120, 999), "variable": 0.0011},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0006},
        {"rango": (90, 99.99), "variable": 0.0007},
        {"rango": (100, 109.99), "variable": 0.0010},
        {"rango": (110, 119.99), "variable": 0.0010},
        {"rango": (120, 999), "variable": 0.0011},
    ],
    "TC": [
        {"rango": (85, 89.99), "variable": 0.0007},
        {"rango": (90, 99.99), "variable": 0.0008},
        {"rango": (100, 109.99), "variable": 0.0011},
        {"rango": (110, 119.99), "variable": 0.0012},
        {"rango": (120, 999), "variable": 0.0012},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0006},
        {"rango": (90, 99.99), "variable": 0.0007},
        {"rango": (100, 109.99), "variable": 0.0010},
        {"rango": (110, 119.99), "variable": 0.0010},
        {"rango": (120, 999), "variable": 0.0011},
    ],
}

comisiones_alternos_A = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0120},
        {"rango": (90, 99.99), "variable": 0.0145},
        {"rango": (100, 109.99), "variable": 0.0176},
        {"rango": (110, 119.99), "variable": 0.0183},
        {"rango": (120, 999), "variable": 0.0189},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0017},
        {"rango": (90, 99.99), "variable": 0.0021},
        {"rango": (100, 109.99), "variable": 0.0025},
        {"rango": (110, 119.99), "variable": 0.0026},
        {"rango": (120, 999), "variable": 0.0027},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0017},
        {"rango": (90, 99.99), "variable": 0.0021},
        {"rango": (100, 109.99), "variable": 0.0025},
        {"rango": (110, 119.99), "variable": 0.0026},
        {"rango": (120, 999), "variable": 0.0027},
    ],
    "TC": [
        {"rango": (85, 89.99), "variable": 0.0019},
        {"rango": (90, 99.99), "variable": 0.0023},
        {"rango": (100, 109.99), "variable": 0.0028},
        {"rango": (110, 119.99), "variable": 0.0029},
        {"rango": (120, 999), "variable": 0.0030},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0017},
        {"rango": (90, 99.99), "variable": 0.0021},
        {"rango": (100, 109.99), "variable": 0.0025},
        {"rango": (110, 119.99), "variable": 0.0026},
        {"rango": (120, 999), "variable": 0.0027},
    ],
}
comisiones_asesores_A = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0107},
        {"rango": (90, 99.99), "variable": 0.0132},
        {"rango": (100, 109.99), "variable": 0.0164},
        {"rango": (110, 119.99), "variable": 0.0170},
        {"rango": (120, 999), "variable": 0.0176},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0015},
        {"rango": (90, 99.99), "variable": 0.0019},
        {"rango": (100, 109.99), "variable": 0.0023},
        {"rango": (110, 119.99), "variable": 0.0024},
        {"rango": (120, 999), "variable": 0.0025},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0015},
        {"rango": (90, 99.99), "variable": 0.0019},
        {"rango": (100, 109.99), "variable": 0.0023},
        {"rango": (110, 119.99), "variable": 0.0024},
        {"rango": (120, 999), "variable": 0.0025},
    ],
    "TC": [
        {"rango": (85, 89.99), "variable": 0.0017},
        {"rango": (90, 99.99), "variable": 0.0021},
        {"rango": (100, 109.99), "variable": 0.0026},
        {"rango": (110, 119.99), "variable": 0.0027},
        {"rango": (120, 999), "variable": 0.0028},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0015},
        {"rango": (90, 99.99), "variable": 0.0019},
        {"rango": (100, 109.99), "variable": 0.0023},
        {"rango": (110, 119.99), "variable": 0.0024},
        {"rango": (120, 999), "variable": 0.0025},
    ],
}
comisiones_admins_B = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0063},
        {"rango": (90, 99.99), "variable": 0.0069},
        {"rango": (100, 109.99), "variable": 0.0076},
        {"rango": (110, 119.99), "variable": 0.0079},
        {"rango": (120, 999), "variable": 0.0082},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0009},
        {"rango": (90, 99.99), "variable": 0.0010},
        {"rango": (100, 109.99), "variable": 0.0011},
        {"rango": (110, 119.99), "variable": 0.0011},
        {"rango": (120, 999), "variable": 0.0012},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0009},
        {"rango": (90, 99.99), "variable": 0.0010},
        {"rango": (100, 109.99), "variable": 0.0011},
        {"rango": (110, 119.99), "variable": 0.0011},
        {"rango": (120, 999), "variable": 0.0012},
    ],
    "TC": [
        {"rango": (85, 89.99), "variable": 0.0010},
        {"rango": (90, 99.99), "variable": 0.0011},
        {"rango": (100, 109.99), "variable": 0.0012},
        {"rango": (110, 119.99), "variable": 0.0013},
        {"rango": (120, 999), "variable": 0.0013},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0009},
        {"rango": (90, 99.99), "variable": 0.0010},
        {"rango": (100, 109.99), "variable": 0.0011},
        {"rango": (110, 119.99), "variable": 0.0011},
        {"rango": (120, 999), "variable": 0.0012},
    ],
}
comisiones_asesores_B = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0113},
        {"rango": (90, 99.99), "variable": 0.0139},
        {"rango": (100, 109.99), "variable": 0.0170},
        {"rango": (110, 119.99), "variable": 0.0176},
        {"rango": (120, 999), "variable": 0.0183},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0016},
        {"rango": (90, 99.99), "variable": 0.0020},
        {"rango": (100, 109.99), "variable": 0.0024},
        {"rango": (110, 119.99), "variable": 0.0025},
        {"rango": (120, 999), "variable": 0.0026},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0016},
        {"rango": (90, 99.99), "variable": 0.0020},
        {"rango": (100, 109.99), "variable": 0.0024},
        {"rango": (110, 119.99), "variable": 0.0025},
        {"rango": (120, 999), "variable": 0.0026},
    ],
    "TC": [
        {"rango": (85, 89.99), "variable": 0.0018},
        {"rango": (90, 99.99), "variable": 0.0022},
        {"rango": (100, 109.99), "variable": 0.0027},
        {"rango": (110, 119.99), "variable": 0.0028},
        {"rango": (120, 999), "variable": 0.0029},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0016},
        {"rango": (90, 99.99), "variable": 0.0020},
        {"rango": (100, 109.99), "variable": 0.0024},
        {"rango": (110, 119.99), "variable": 0.0025},
        {"rango": (120, 999), "variable": 0.0026},
    ],
}
comisiones_admins_kioscos = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0047, "fijo": 737},
        {"rango": (90, 99.99), "variable": 0.0054, "fijo": 871},
        {"rango": (100, 109.99), "variable": 0.0074, "fijo": 1005},
        {"rango": (110, 119.99), "variable": 0.0161, "fijo": 1139},
        {"rango": (120, 999), "variable": 0.0168, "fijo": 1206},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0008, "fijo": 121},
        {"rango": (90, 99.99), "variable": 0.0009, "fijo": 143},
        {"rango": (100, 109.99), "variable": 0.0012, "fijo": 165},
        {"rango": (110, 119.99), "variable": 0.0026, "fijo": 187},
        {"rango": (120, 999), "variable": 0.0028, "fijo": 198},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0008, "fijo": 121},
        {"rango": (90, 99.99), "variable": 0.0009, "fijo": 143},
        {"rango": (100, 109.99), "variable": 0.0012, "fijo": 165},
        {"rango": (110, 119.99), "variable": 0.0026, "fijo": 187},
        {"rango": (120, 999), "variable": 0.0028, "fijo": 198},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0008, "fijo": 121},
        {"rango": (90, 99.99), "variable": 0.0009, "fijo": 143},
        {"rango": (100, 109.99), "variable": 0.0012, "fijo": 165},
        {"rango": (110, 119.99), "variable": 0.0026, "fijo": 187},
        {"rango": (120, 999), "variable": 0.0028, "fijo": 198},
    ],
}
comisiones_asesores_kioscos = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0121, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0147, "fijo": 603},
        {"rango": (100, 109.99), "variable": 0.0181, "fijo": 737},
        {"rango": (110, 119.99), "variable": 0.0188, "fijo": 871},
        {"rango": (120, 999), "variable": 0.0194, "fijo": 1005},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0020, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0024, "fijo": 99},
        {"rango": (100, 109.99), "variable": 0.0030, "fijo": 121},
        {"rango": (110, 119.99), "variable": 0.0031, "fijo": 143},
        {"rango": (120, 999), "variable": 0.0032, "fijo": 165},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0020, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0024, "fijo": 99},
        {"rango": (100, 109.99), "variable": 0.0030, "fijo": 121},
        {"rango": (110, 119.99), "variable": 0.0031, "fijo": 143},
        {"rango": (120, 999), "variable": 0.0032, "fijo": 165},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0020, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0024, "fijo": 99},
        {"rango": (100, 109.99), "variable": 0.0030, "fijo": 121},
        {"rango": (110, 119.99), "variable": 0.0031, "fijo": 143},
        {"rango": (120, 999), "variable": 0.0032, "fijo": 165},
    ],
}


# Función para calcular cumplimiento y aplicar porcentaje

def calcular_comision(tabla, indicador, meta, logro, venta_total):
    if meta == 0:
        st.warning(f"⚠️ Meta para {indicador} es 0. No se puede calcular.")
        return 0

    porcentaje = (logro / meta) * 100
    for tramo in tabla[indicador]:
        min_r, max_r = tramo["rango"]
        if min_r <= porcentaje <= max_r:
            return round(venta_total * tramo["variable"], 2)
    st.warning(f"⚠️ No se encontró un tramo para {indicador} con {round(porcentaje, 2)}%")
    return 0

# --- INTERFAZ STREAMLIT ---
st.title("📊 Simulador de Comisiones Vélez")

# 🧍‍♂️ Nombre del colaborador
nombre = st.text_input("Nombre del colaborador")

# Ingreso básico
tienda = st.selectbox("Selecciona tu tienda", list(TIENDAS_VELEZ.keys()))
tipo_tienda = TIENDAS_VELEZ[tienda]

# Mostrar resumen
st.success(f"🧍 {nombre} - Cargo: {cargo} - Tienda: {tienda} ({tipo_tienda})")

cargo = st.selectbox("Selecciona tu cargo", ["Administrador", "Alterno", "Asesor"])
venta = st.number_input("Venta total lograda (Q)", min_value=0.0)

# Ingreso de indicadores
indicadores = {}
for indicador in ["PPTO", "VxF", "AxF", "TC", "Fidelizacion"]:
    meta = st.number_input(f"Meta {indicador}", min_value=0.0, key=f"meta_{indicador}")
    logro = st.number_input(f"Logro {indicador}", min_value=0.0, key=f"logro_{indicador}")
    indicadores[indicador] = (meta, logro)

# Selección de tabla según cargo y tipo de tienda
if cargo == "Administrador" and tipo_tienda == "A":
    tabla = comisiones_admins_A
elif cargo == "Administrador" and tipo_tienda == "B":
    tabla = comisiones_admins_B
elif cargo == "Administrador" and tipo_tienda == "Kiosco":
    tabla = comisiones_admins_kioscos
elif cargo == "Alterno" and tipo_tienda == "A":
    tabla = comisiones_alternos_A
elif cargo == "Asesor" and tipo_tienda == "A":
    tabla = comisiones_asesores_A
elif cargo == "Asesor" and tipo_tienda == "B":
    tabla = comisiones_asesores_B
elif cargo == "Asesor" and tipo_tienda == "Kiosco":
    tabla = comisiones_asesores_kioscos
else:
    st.error("No hay tabla definida para esta combinación de cargo y tienda.")
    st.stop()

if st.button("Calcular Comisión"):
    total = 0
    for indicador, (meta, logro) in indicadores.items():
        comision = calcular_comision(tabla, indicador, meta, logro, venta)
        total += comision
        st.success(f"{indicador}: Q{comision}")

    st.markdown("---")
    st.markdown(f"<h2 style='color:green;'>💰 Comisión Total: Q{round(total, 2)}</h2>", unsafe_allow_html=True)

# Pie
st.markdown("---")
st.markdown("<div style='text-align:center; opacity: 0.6;'>Desarrollado por Edgar Urrutia - Proyecto Formación - Dinegma 2025</div>", unsafe_allow_html=True)
