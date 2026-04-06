# Recomendador musical para mejorar el bienestar 🎵

Sistema de recomendación musical orientado a bienestar emocional, construido a partir de un cuestionario de hábitos de escucha, variables de salud mental autopercibida y preferencias musicales. El proyecto combina **clasificación supervisada** para estimar probabilidad de mejora del estado de ánimo y **clustering** para segmentar perfiles de usuario y enriquecer la recomendación.

## Tabla de contenidos
1. [Objetivo](#objetivo)
2. [Problema de negocio](#problema-de-negocio)
3. [Arquitectura del proyecto](#arquitectura-del-proyecto)
4. [Estructura del repositorio](#estructura-del-repositorio)
5. [Stack tecnológico](#stack-tecnológico)
6. [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
7. [App Streamlit](#app-streamlit)
8. [Datos](#datos)
9. [Metodología](#metodología)
10. [Resultados esperados](#resultados-esperados)
11. [Limitaciones](#limitaciones)
12. [Próximos pasos](#próximos-pasos)

## Objetivo

Desarrollar un sistema capaz de:
- estimar si un perfil de usuario tiene **probabilidad de mejorar su estado de ánimo** con música,
- segmentar usuarios según hábitos y señales emocionales,
- traducir ese scoring en una experiencia web sencilla basada en cuestionario.

## Problema de negocio

En contextos de bienestar digital, contenido personalizado y health-tech ligera, una recomendación genérica tiene poco valor. Este proyecto busca responder a una pregunta concreta:

> **¿Podemos personalizar recomendaciones musicales basándonos en hábitos de escucha, variables emocionales y patrones de género para aumentar la probabilidad de mejora percibida?**

## Arquitectura del proyecto

El proyecto está planteado en dos capas:

### 1) Modelo predictivo
Clasificador supervisado para estimar `target_improve`, variable derivada de la respuesta `music_effects`.

### 2) Segmentación de usuarios
Clustering con KMeans para enriquecer la lógica de recomendación con perfiles interpretables.

### 3) Aplicación web
Interfaz en **Streamlit** con formulario web para:
- capturar respuestas del usuario,
- transformarlas al formato del modelo,
- cargar artefactos serializados,
- devolver scoring y recomendación.

## Estructura del repositorio

```bash
"pendiente"
```

## Stack tecnológico

- Python
- pandas
- numpy
- scikit-learn
- imbalanced-learn
- matplotlib
- streamlit
- joblib

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPO>
cd repo_template_recomendador_musical
```

### 2. Crear entorno virtual
```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Lanzar la app
```bash
streamlit run app/app.py
```

## App Streamlit

La app incluida en este repositorio es una **plantilla funcional de front + inferencia**.

### Qué hace ya
- renderiza un formulario web,
- recoge las variables principales del notebook,
- aplica una transformación básica,
- intenta cargar artefactos desde `models/`.

### Qué falta para que prediga con el modelo real
Debes exportar desde el notebook al menos estos artefactos:

- `models/model_pipeline.joblib`
- `models/threshold.json`
- opcionalmente:
  - `models/kmeans.joblib`
  - `models/cluster_metadata.csv`
  - `models/spotify_catalog.csv`

## Datos

### Fuentes contempladas en el notebook
- `mxmh_survey_results.csv`
- `musica_bienestar_results.csv`
- dataset de canciones para recomendación final

> No incluyas datasets privados, sensibles o pesados directamente en GitHub si no tienes permiso o si exceden el tamaño razonable del repo.

## Metodología

A partir del notebook actual, el pipeline contiene estas fases:

1. **Carga e integración de datos**
2. **Normalización de columnas**
3. **Limpieza y tipado**
4. **Feature engineering**
   - `mental_health_score`
   - `high_anxiety_flag`
   - `listener_intensity`
   - `genre_score_total`
   - `is_musician`
   - `dominant_genre`
   - `genre_diversity`
5. **Entrenamiento de modelo supervisado**
6. **Ajuste de threshold**
7. **Validación**
8. **Clustering**
9. **Lógica de recomendación**

## Resultados esperados

Cuando conectes los artefactos reales, la app debería permitir:
- estimar una probabilidad de mejora,
- decidir si el usuario entra en el segmento “recomendable”,
- asociar ese usuario a un cluster,
- proponer géneros o canciones.

## Limitaciones

- La plantilla actual **no exporta automáticamente el modelo desde el notebook**.
- El notebook contiene lógica exploratoria y lógica final mezcladas; conviene modularizar.
- La app incluida usa una vía de inferencia robusta, pero depende de que serialices los artefactos reales.

## Próximos pasos

- extraer preprocessing e inferencia del notebook a `src/`,
- guardar artefactos con `joblib`,
- añadir catálogo musical limpio para recomendación final,
- incorporar trazabilidad de experimentos,
- desplegar en Streamlit Community Cloud o Render.

## Autor

Juan Carlos Lara Gallego
https://github.com/JuanCarlosLaraGallego
https://www.linkedin.com/in/juancarloslaragallego/
