import streamlit as st
import pandas as pd

from src.features import get_frequency_columns
from src.inference import predict_user

st.set_page_config(
    page_title="Recomendador musical y bienestar",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Recomendador musical para mejorar el bienestar")
st.caption("Plantilla profesional de app en Streamlit conectada a tu pipeline de ML.")

st.markdown(
    """
Esta app recoge las respuestas del usuario, construye el vector de entrada y trata de cargar
los artefactos del modelo desde la carpeta `models/`.

**Estado actual de la plantilla**
- ✅ formulario operativo
- ✅ transformación de variables base
- ✅ inferencia preparada
- ⏳ pendiente conectar artefactos reales exportados desde el notebook
"""
)

with st.form("wellbeing_music_form"):
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
st.markdown(
    """
### Siguiente paso técnico recomendado
Exporta desde el notebook:
```python
import joblib, json
joblib.dump(model_pipeline, "models/model_pipeline.joblib")
with open("models/threshold.json", "w", encoding="utf-8") as f:
    json.dump({"threshold": 0.60}, f)
```
"""
)
