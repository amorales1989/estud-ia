import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Cliente OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Configuración
st.set_page_config(page_title="StudyAI", page_icon="📚")


# UI
st.title("📚 StudyAI - Asistente Inteligente de Estudio")

texto_usuario = st.text_area("✍️ Pegá el texto:", height=200)

opcion = st.selectbox(
    "¿Qué querés generar?",
    ["Todo", "Resumen", "Explicación", "Preguntas"]
)

# Botón
if st.button("🚀 Generar"):
    if texto_usuario.strip() == "":
        st.warning("Ingresá un texto.")
    else:
        with st.spinner("Pensando..."):

            if opcion == "Resumen":
                tarea = "Genera un resumen claro en máximo 150 palabras."
            elif opcion == "Explicación":
                tarea = "Explica los conceptos de forma sencilla."
            elif opcion == "Preguntas":
                tarea = "Genera 3 preguntas tipo examen con respuestas."
            else:
                tarea = """
                1. Resumen claro (máx 150 palabras)
                2. Explicación sencilla
                3. 3 preguntas con respuestas
                """

            prompt = f"""
            Actúa como profesor experto.

            Texto:
            {texto_usuario}

            Tareas:
            {tarea}

            Responde ordenado.
            """

            try:
                response = client.chat.completions.create(
                    model="meta-llama/llama-3-8b-instruct",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

                resultado = response.choices[0].message.content

                st.success("✅ Resultado:")
                st.write(resultado)

            except Exception as e:
                st.error(f"Error: {e}")