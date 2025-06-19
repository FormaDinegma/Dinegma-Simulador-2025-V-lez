import streamlit as st

# --- TABLAS DE COMISIONES ---

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

# (Aquí continuarías con las tablas para Alterno A, Asesores A, Admins B, Asesores B, Kioscos...)

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

# Ingreso básico
tienda = st.selectbox("Selecciona tu tienda", list(range(1, 6)))
cargo = st.selectbox("Selecciona tu cargo", ["Administrador"])  # Puedes ampliar esto
venta = st.number_input("Venta total lograda (Q)", min_value=0.0)

# Ingreso de indicadores
indicadores = {}
for indicador in ["PPTO", "VxF", "AxF", "TC", "Fidelizacion"]:
    meta = st.number_input(f"Meta {indicador}", min_value=0.0, key=f"meta_{indicador}")
    logro = st.number_input(f"Logro {indicador}", min_value=0.0, key=f"logro_{indicador}")
    indicadores[indicador] = (meta, logro)

# Simular cálculo para Admin A
tabla = comisiones_admins_A

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
