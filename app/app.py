import sys
from pathlib import Path

import streamlit as st
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.features import get_frequency_columns
from src.inference import predict_user

st.set_page_config(
    page_title="Recomendador musical y bienestar",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Recomendador musical para mejorar el bienestar")
st.caption("Plantilla profesional de app en Streamlit conectada a tu pipeline de ML.")
st.warning("""
DISCLAIMER

Aviso importante sobre este sistema de recomendación

Este sistema no es una herramienta clínica ni un diagnóstico de salud mental. Su función es estimar, a partir de tu perfil de hábitos musicales y bienestar auto-reportado, si personas con características similares a las tuyas tienden a percibir una mejora en su estado de ánimo al escuchar música.

Las recomendaciones se basan en patrones estadísticos extraídos de una encuesta de 845 usuarios. Cuando el sistema decide recomendarte música, significa que tu perfil coincide con el de personas que reportaron ese efecto positivo — no que la música vaya a mejorar tu estado de ánimo de forma garantizada.

El modelo alcanza aproximadamente un 84% de precisión en la identificación de perfiles que podrían beneficiarse, lo que implica que en algunos casos puede recomendar a usuarios que no perciben ese beneficio, o no recomendar a otros que sí lo harían.

Si estás atravesando una situación de salud mental que requiere atención, este sistema no sustituye en ningún caso la valoración de un profesional.
""")

ºwith st.form("wellbeing_music_form"):
    st.subheader("1) Perfil general")
    age = st.slider("Edad", min_value=12, max_value=80, value=25)
    hours_per_day = st.slider("Horas de escucha al día", min_value=0.0, max_value=12.0, value=2.0, step=0.5)
    bpm = st.number_input("BPM habitual aproximado", min_value=40, max_value=220, value=120)

    st.subheader("2) Hábitos de escucha")
    primary_streaming_service = st.selectbox(
        "Plataforma principal",
        ["Spotify", "YouTube Music", "Apple Music", "SoundCloud", "Other"]
    )
    while_working = st.selectbox("¿Escuchas música mientras trabajas o estudias?", ["yes", "no"])
    instrumentalist = st.selectbox("¿Tocas algún instrumento?", ["yes", "no"])
    composer = st.selectbox("¿Compones música?", ["yes", "no"])
    exploratory = st.selectbox("¿Te gusta explorar música nueva?", ["yes", "no"])
    foreign_languages = st.selectbox("¿Escuchas música en otros idiomas?", ["yes", "no"])

    st.subheader("3) Estado emocional autopercibido")
    anxiety = st.slider("Ansiedad", 0, 10, 5)
    depression = st.slider("Depresión", 0, 10, 5)
    insomnia = st.slider("Insomnio", 0, 10, 3)
    ocd = st.slider("OCD", 0, 10, 1)

    st.subheader("4) Preferencias")
    fav_genre = st.selectbox(
        "Género favorito",
        [
            "Classical", "Country", "EDM", "Folk", "Gospel", "Hip hop", "Jazz",
            "K pop", "Latin", "Lofi", "Metal", "Pop", "R&B", "Rap", "Rock",
            "Video game music"
        ]
    )

    st.subheader("5) Frecuencia por género")
    freq_options = ["never", "rarely", "sometimes", "frequently", "very frequently"]
    genre_inputs = {}
    pretty_labels = {
        "frequency_classical": "Classical",
        "frequency_country": "Country",
        "frequency_edm": "EDM",
        "frequency_folk": "Folk",
        "frequency_gospel": "Gospel",
        "frequency_hip_hop": "Hip hop",
        "frequency_jazz": "Jazz",
        "frequency_k_pop": "K pop",
        "frequency_latin": "Latin",
        "frequency_lofi": "Lofi",
        "frequency_metal": "Metal",
        "frequency_pop": "Pop",
        "frequency_r&b": "R&B",
        "frequency_rap": "Rap",
        "frequency_rock": "Rock",
        "frequency_video_game_music": "Video game music",
    }

    for col in get_frequency_columns():
        genre_inputs[col] = st.selectbox(pretty_labels[col], freq_options, index=2)

    submitted = st.form_submit_button("Evaluar perfil")

if submitted:
    payload = {
        "age": age,
        "primary_streaming_service": primary_streaming_service,
        "hours_per_day": hours_per_day,
        "while_working": while_working,
        "instrumentalist": instrumentalist,
        "composer": composer,
        "fav_genre": fav_genre,
        "exploratory": exploratory,
        "foreign_languages": foreign_languages,
        "bpm": bpm,
        "anxiety": anxiety,
        "depression": depression,
        "insomnia": insomnia,
        "ocd": ocd,
        **genre_inputs,
    }

    result = predict_user(payload)

    st.divider()
    st.subheader("Resultado")

    if result["status"] == "missing_model":
        st.warning(result["message"])
        st.write("Threshold configurado:", result["threshold"])
        with st.expander("Ver features construidas por la plantilla"):
            st.write(result["features_used"])
    else:
        probability = result["probability_improve"]
        recommend_flag = result["recommend_flag"]
        threshold = result["threshold"]

        st.metric("Probabilidad estimada de mejora", f"{probability:.1%}")
        st.write(f"Threshold aplicado: `{threshold:.2f}`")

        if recommend_flag == 1:
            st.success("Perfil elegible para recomendación musical personalizada.")
        else:
            st.info("Perfil no marcado como prioritario según el threshold actual.")

        with st.expander("Ver features usadas en inferencia"):
            st.write(result["features_used"])

st.divider()


