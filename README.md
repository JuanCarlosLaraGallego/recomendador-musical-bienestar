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

##  Objetivo del proyecto

Desarrollar un sistema de recomendación musical orientado al bienestar emocional, capaz de estimar si un usuario tiene probabilidad de mejorar su estado de ánimo en función de sus hábitos musicales y variables de salud mental auto-reportadas.

El sistema combina:

- Machine Learning supervisado (clasificación)
- Feature engineering sobre hábitos de escucha
- Aplicación interactiva en Streamlit

##  Problema de negocio

Muchas personas utilizan la música como herramienta para mejorar su estado de ánimo, pero no existe una forma estructurada de identificar qué perfiles se benefician más de este efecto.

Este proyecto busca:

- Detectar perfiles con mayor probabilidad de mejora
- Sentar las bases para recomendaciones musicales personalizadas
- Traducir datos subjetivos en decisiones accionables

## Arquitectura del proyecto

##  Cómo funciona

1. El usuario completa un cuestionario
2. Se transforman las variables mediante feature engineering
3. Se aplica un modelo de Machine Learning (Random Forest)
4. Se calcula la probabilidad de mejora
5. Se genera una recomendación basada en un threshold

##  Documentación

Puedes consultar la documentación completa del proyecto aquí:

👉 [Ver documentación completa](docs/README.md)

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
