# Descripción de los Datos

## Visión General

Este proyecto se basa en el dataset **Music & Mental Health (MxMH)**, que analiza la relación entre los hábitos de escucha musical y la salud mental auto-reportada.

El dataset ha sido **limpiado y transformado** para adaptarlo a análisis exploratorio y modelado de machine learning.

---

## Aviso Importante

Los indicadores de salud mental son **auto-reportados** y el tamaño de la muestra es relativamente reducido (~800 usuarios).

Por tanto:
- Los resultados deben interpretarse con cautela
- No son generalizables a toda la población
- Representan **patrones indicativos**, no evidencia clínica

---

## Fuentes de Datos

### 1. Dataset de Encuesta (MxMH)
- Recogido mediante formulario online
- Distribuido en redes sociales (Reddit, Discord, etc.)
- Contiene:
  - Hábitos musicales
  - Preferencias de género
  - Variables de salud mental

### 2. Dataset de Spotify
Utilizado para el sistema de recomendación:
- Información de canciones
- Features musicales
- Género y metadatos

---

## Estructura del Dataset

### Bloque 1 — Perfil y hábitos
- Edad
- Plataforma de streaming
- Horas de escucha
- BPM

### Bloque 2 — Preferencias musicales
- Género favorito
- Frecuencia de escucha por género

### Bloque 3 — Salud mental
- Ansiedad
- Depresión
- Insomnio
- OCD

---

## Variable Objetivo

### `music_effects` (transformada)

Original:
- Improve
- No effect
- Worsen

Transformación final:
- `1 → Mejora`
- `0 → No mejora`

---

## Notas Clave

- El dataset ha sido procesado antes del modelado
- Se han aplicado transformaciones para alinear con ML