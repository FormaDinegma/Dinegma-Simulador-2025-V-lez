import streamlit as st

# --- Tiendas y Tipos ---
tiendas_por_tipo = {
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

# --- App UI ---
st.title("Simulador de Comisiones Vélez")

nombre = st.text_input("Nombre del colaborador")
cargo = st.selectbox("Cargo", ["Administrador", "Alterno", "Asesor"])
tienda = st.selectbox("Tienda", list(tiendas_por_tipo.keys()))
tipo_tienda = tiendas_por_tipo[tienda]

st.markdown(f"**Tipo de Tienda Detectado:** {tipo_tienda}")

# Función para ingreso de metas y logros
def ingreso_indicadores(indicador):
    col1, col2 = st.columns(2)
    with col1:
        meta = st.number_input(f"Meta {indicador}", min_value=0.0, step=0.01, key=f"meta_{indicador}")
    with col2:
        logro = st.number_input(f"Logro {indicador}", min_value=0.0, step=0.01, key=f"logro_{indicador}")
    return meta, logro

meta_ppto, logro_ppto = ingreso_indicadores("PPTO")

# --- Cálculos ---
def calcular_cumplimiento(meta, logro):
    return (logro / meta) * 100 if meta != 0 else 0

def obtener_comision_y_fijo(cargo, tipo_tienda, indicador, cumplimiento):
    cumplimiento = round(cumplimiento, 2)
    comisiones = {
        "Administrador": {
            "A": {
                "PPTO": [
                    (85, 89.99, 0.44),
                    (90, 99.99, 0.50),
                    (100, 109.99, 0.69),
                    (110, 119.99, 0.72),
                    (120, float('inf'), 0.76),
                ]
            },
            "Kiosco": {
                "PPTO": [
                    (85, 89.99, 0.47, 737),
                    (90, 99.99, 0.54, 871),
                    (100, 109.99, 0.74, 1005),
                    (110, 119.99, 1.61, 1139),
                    (120, float('inf'), 1.68, 1206),
                ]
            }
        },
        "Asesor": {
            "Kiosco": {
                "PPTO": [
                    (85, 89.99, 1.21, 77),
                    (90, 99.99, 1.47, 603),
                    (100, 109.99, 1.81, 737),
                    (110, 119.99, 1.88, 871),
                    (120, float('inf'), 1.94, 1005),
                ]
            }
        }
    }

    try:
        reglas = comisiones[cargo][tipo_tienda][indicador]
        for regla in reglas:
            if regla[0] <= cumplimiento <= regla[1]:
                return (regla[2], regla[3]) if len(regla) == 4 else (regla[2], None)
    except KeyError:
        return 0.0, None

# --- Resultado para PPTO ---
if nombre and tienda:
    cumplimiento_ppto = calcular_cumplimiento(meta_ppto, logro_ppto)
    porcentaje, fijo = obtener_comision_y_fijo(cargo, tipo_tienda, "PPTO", cumplimiento_ppto)

    st.subheader("Resultado Comisión PPTO")
    st.write(f"Cumplimiento: {cumplimiento_ppto:.2f}%")
    st.write(f"Porcentaje de comisión: {porcentaje}%")
    if fijo is not None:
        st.write(f"Monto fijo garantizado (si el porcentaje da menos): Q{fijo}")

# --- Pie de página ---
st.markdown("---")
st.markdown(
    "<div style='text-align:center; opacity: 0.6;'>Desarrollado por Edgar Urrutia - Proyecto Formación - Dinegma 2025</div>",
    unsafe_allow_html=True
)
