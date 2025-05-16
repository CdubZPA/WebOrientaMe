import streamlit as st
import pandas as pd

# Configuración de la página con título y diseño centrado
st.set_page_config(page_title="OrientaMe", layout="centered")

# Inicializar el estado de navegación si no existe
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'inicio'

# Función para mostrar la página de inicio
def mostrar_inicio():
    st.title("🎓 ¡Bienvenido a OrientaMe!")
    st.text("OrientaMe fue diseñado con el fin de guiarte a ti, para que puedas quitarte de esa frustracion de no poder definirte por algo en particular, nosotras hacemos que tengas un objetivo que alcanzar, TODO EN ESTA VIDA SE PUEDE, ¡ANIMOS!.")
    st.subheader("¿Qué deseas hacer?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Buscar una carrera"):
            st.session_state.pagina = 'buscar'

    with col2:
        if st.button("💡 Ver consejos"):
            st.session_state.pagina = 'consejos'

# Función para mostrar la página de consejos
def mostrar_consejos():
    st.title("💡 Consejos de Orientación")
    st.write("Aquí puedes mostrar consejos útiles sobre cómo elegir una carrera, hábitos de estudio, manejo del tiempo, etc.")
    st.markdown("- Conócete a ti mismo: identifica tus fortalezas e intereses.")
    st.markdown("- Investiga las carreras y sus salidas laborales.")
    st.markdown("- Consulta con profesionales o estudiantes avanzados.")
    st.markdown("- Evalúa universidades según tus necesidades y recursos.")

    if st.button("⬅️ Volver al inicio"):
        st.session_state.pagina = 'inicio'

# Función para mostrar la página de búsqueda de carreras (contenido actual)
def mostrar_busqueda():
    st.title("🎓 OrientaMe: Recomendador de Carreras")

    st.header("Ingresa tus datos y puntajes")

    # Puntajes por área específica del ICFES
    area_mates = st.number_input("Puntaje Área Matemáticas:", 0, 100, 50)
    ingles = st.number_input("Puntaje Inglés:", 0, 100, 50)
    lectura_critica = st.number_input("Puntaje Lectura Crítica:", 0, 100, 50)
    sociales = st.number_input("Puntaje Sociales y Ciudadanas:", 0, 100, 50)
    ciencias = st.number_input("Puntaje Ciencias Naturales:", 0, 100, 50)

    # Calcular automáticamente el puntaje global
    icfes = area_mates + ingles + lectura_critica + sociales + ciencias
    st.markdown(f"**Puntaje total ICFES:** {icfes}")

    # Intereses
    a_intereses = ["Tecnología", "Diseño", "Salud", "Negocios", "Arte", "Ciencia"]
    intereses = st.multiselect("Selecciona tus intereses:", options=a_intereses, default=["Tecnología"])

    if st.button("Obtener recomendaciones"):
        carreras = {
            "Ingeniería de Sistemas": icfes * 0.4 + area_mates * 0.2 + ingles * 0.1 + lectura_critica * 0.1 + ciencias * 0.1 + sociales * 0.1 + (50 if "Tecnología" in intereses else 0),
            "Arquitectura": icfes * 0.3 + area_mates * 0.1 + ingles * 0.05 + lectura_critica * 0.1 + ciencias * 0.05 + sociales * 0.1 + (50 if "Diseño" in intereses else 0),
            "Medicina": icfes * 0.35 + area_mates * 0.05 + ingles * 0.05 + lectura_critica * 0.1 + ciencias * 0.3 + sociales * 0.1 + (50 if "Salud" in intereses else 0),
            "Administración": icfes * 0.3 + area_mates * 0.1 + ingles * 0.1 + lectura_critica * 0.1 + ciencias * 0.05 + sociales * 0.2 + (50 if "Negocios" in intereses else 0),
            "Artes Plásticas": icfes * 0.25 + area_mates * 0.05 + ingles * 0.05 + lectura_critica * 0.1 + ciencias * 0.05 + sociales * 0.1 + (50 if "Arte" in intereses else 0),
            "Física": icfes * 0.4 + area_mates * 0.3 + ingles * 0.05 + lectura_critica * 0.1 + ciencias * 0.1 + sociales * 0.05 + (50 if "Ciencia" in intereses else 0)
        }

        df = pd.DataFrame.from_dict(carreras, orient="index", columns=["Puntaje"]).sort_values(by="Puntaje", ascending=False)

        st.subheader("📊 Top 5 Carreras")
        st.bar_chart(df.head(5))
        st.table(df.head(5))

        mejor = df.index[0]
        st.markdown(f"### 🎯 Tu mejor opción: **{mejor}**")
        st.write("Más información sobre esta carrera... (aquí podrías añadir descripción, plan de estudios, consejos)")

    if st.button("⬅️ Volver al inicio"):
        st.session_state.pagina = 'inicio'

# Enrutamiento entre páginas
if st.session_state.pagina == 'inicio':
    mostrar_inicio()
elif st.session_state.pagina == 'consejos':
    mostrar_consejos()
elif st.session_state.pagina == 'buscar':
    mostrar_busqueda()

# Información en el sidebar
st.sidebar.info("OrientaMe - Proyecto universitario | Hecho con Streamlit")