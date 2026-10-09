import streamlit as st

st.set_page_config(page_title="Detector de Riesgo de Rotación", page_icon="📊")

st.title("📊 Detector de Riesgo de Rotación de Empleados")
st.write("Herramienta de apoyo para profesionales de Recursos Humanos.")

st.header("Datos del empleado")

edad = st.number_input("Edad", min_value=18, max_value=70, value=30)
antiguedad = st.number_input("Antigüedad en la empresa (años)", min_value=0, max_value=40, value=5)
departamento = st.selectbox("Departamento", ["Administración", "Finanzas", "Operaciones", "Marketing", "IT", "RRHH"])
salario = st.number_input("Salario anual (€)", min_value=15000, max_value=150000, value=30000)
desempeno = st.slider("Nivel de desempeño", 1, 5, 3)
compromiso = st.slider("Nivel de compromiso", 1, 5, 3)
promociones = st.number_input("Número de promociones recibidas", 0, 10, 0)
formacion = st.number_input("Horas de formación realizadas en el último año", 0, 200, 20)
horas_extra = st.number_input("Horas extraordinarias al mes", 0, 100, 10)
modalidad = st.selectbox("Modalidad de trabajo", ["Presencial", "Híbrida", "Remota"])
absentismo = st.number_input("Días de absentismo durante el último año", 0, 60, 2)

if st.button("Analizar riesgo"):
    puntuacion = 0
    factores = []
    recomendaciones = []

    if compromiso <= 2:
        puntuacion += 3
        factores.append("Bajo nivel de compromiso")
        recomendaciones.append("Desarrollar acciones para aumentar el engagement")
    if desempeno <= 2:
        puntuacion += 2
        factores.append("Nivel de desempeño reducido")
    if promociones == 0 and antiguedad > 5:
        puntuacion += 2
        factores.append("Ausencia de promociones")
    if horas_extra > 20:
        puntuacion += 2
        factores.append("Exceso de horas extraordinarias")
    if absentismo > 10:
        puntuacion += 2
        factores.append("Nivel elevado de absentismo")
    if formacion < 10:
        puntuacion += 1
        factores.append("Escasa formación reciente")

    if puntuacion <= 3:
        riesgo, color = "BAJO", "green"
    elif puntuacion <= 6:
        riesgo, color = "MEDIO", "orange"
    else:
        riesgo, color = "ALTO", "red"

    st.markdown(f"<h2 style='color:{color};'>Riesgo de rotación: {riesgo}</h2>", unsafe_allow_html=True)
    st.subheader("Factores identificados")
    for f in factores:
        st.write("•", f)

    st.subheader("Recomendaciones")
    for r in recomendaciones:
        st.write("•", r)
