# Arquitectura de la Aplicación

## Visión General

La aplicación integra un modelo de ML con una interfaz web en Streamlit.

---

## Flujo

1. Usuario completa formulario
2. Se transforman los datos
3. Se carga el modelo
4. Se calcula probabilidad
5. Se muestra resultado

---

## Componentes

### Frontend
- Streamlit (`app.py`)

### Backend
- `features.py`
- `inference.py`

### Modelo
- Archivo `.joblib`

---

## Salida

- Probabilidad de mejora
- Decisión basada en threshold

---

## Extensión futura

- Sistema de recomendación musical