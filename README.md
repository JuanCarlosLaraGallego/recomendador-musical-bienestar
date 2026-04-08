# Recomendador musical para mejorar el bienestar 🎵

Este proyecto desarrolla un sistema de Machine Learning capaz de estimar si un usuario tiene probabilidad de mejorar su estado de ánimo a través de la música, y en función de ello generar recomendaciones musicales personalizadas.

A diferencia de los recomendadores tradicionales, este sistema no se basa únicamente en preferencias musicales, sino que incorpora variables de comportamiento y estado emocional autopercibido para ofrecer recomendaciones más relevantes.

Demo de la aplicación

👉 Accede a la app aquí:
(https://recomendador-musical-bienestar-7uymm8rhh9khq5gyc42maw.streamlit.app/)

# Cómo funciona

El usuario introduce su perfil:
- hábitos de escucha
- estado emocional
- preferencias musicales
- 
El modelo de Machine Learning:
- analiza el perfil
- determina si el usuario es elegible para recomendación

Si se cumple el criterio:
- se activa el sistema de recomendación
- se generan 10 canciones personalizadas

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

#  Arquitectura
  app/ → interfaz Streamlit
  src/features.py → ingeniería de variables
  src/inference.py → lógica de predicción
  src/recommender.py → sistema de recomendación
  models/ → modelo entrenado + catálogo Spotify

# Modelo
Algoritmo: Random Forest Classifier
Problema: Clasificación binaria
Output: elegibilidad para recomendación

# Sistema de recomendación (V1)
Filtrado por género
Ordenación por popularidad
Top 10 canciones

# Datos
Dataset principal: Music & Mental Health
Dataset adicional: catálogo de canciones Spotify

# Disclaimer

Este sistema no es una herramienta clínica ni un diagnóstico de salud mental. Las recomendaciones se basan en patrones estadísticos y no garantizan resultados individuales.

## Stack tecnológico

- Python
- pandas
- numpy
- scikit-learn
- imbalanced-learn
- matplotlib
- streamlit
- joblib

## Estado del proyecto

✔ Modelo entrenado
✔ App funcional
✔ Recomendador integrado
🔄 Mejora futura del recomendador (ML-based)

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
